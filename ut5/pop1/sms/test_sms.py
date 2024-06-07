import sqlite3
from pathlib import Path
from types import GeneratorType

import pytest
from sms import SIM, SMS, DbHandler, SMSError

TEST_DB_PATH = 'test_sms.db'

# **************************************************************
# FIXTURES
# **************************************************************


@pytest.fixture(autouse=True)
def create_test_database():
    db = Path(TEST_DB_PATH)
    db.unlink(missing_ok=True)
    handler = DbHandler(TEST_DB_PATH)
    handler.create_db()
    sql = """INSERT INTO access VALUES("675118923", "1167", "435512");
INSERT INTO access VALUES("665477232", "2197", "782881")"""
    handler.cur.executescript(sql)
    yield
    db = Path(TEST_DB_PATH)
    db.unlink(missing_ok=True)


@pytest.fixture(autouse=True)
def make_dbhandler_use_test_database(monkeypatch: pytest.MonkeyPatch):
    sconnect = sqlite3.connect

    def mock_sqlite3_connect(*args, **kwargs):
        return sconnect(TEST_DB_PATH)

    monkeypatch.setattr(sqlite3, 'connect', mock_sqlite3_connect)


@pytest.fixture
def sim1():
    return SIM('675118923')


@pytest.fixture
def sim2():
    return SIM('665477232')


@pytest.fixture
def sms1():
    return SMS(
        sender='675118923',
        recipient='721895643',
        message='Hi there. Are you ok?',
    )


@pytest.fixture
def db_con():
    con = sqlite3.connect(TEST_DB_PATH)
    con.row_factory = sqlite3.Row
    yield con
    con.close()


# **************************************************************
# TESTS
# **************************************************************

# --------------------
# Tests para DBHandler
# --------------------


def test_create_db(db_con: sqlite3.Connection):
    TABLES = {
        'access': ('phone_number', 'pin', 'puk'),
        'activity': ('id', 'sender', 'recipient', 'message'),
    }
    assert Path(TEST_DB_PATH).exists()
    cur = db_con.cursor()
    for table, columns in TABLES.items():
        sql = "SELECT ? FROM sqlite_schema WHERE type = 'table'"
        assert cur.execute(sql, [table]).fetchone() is not None
        sql = f"PRAGMA table_info('{table}')"
        for column in columns:
            assert column in [c['name'] for c in cur.execute(sql)]


# --------------
# Tests para SMS
# --------------


def test_build_sms(sms1: SMS):
    assert isinstance(sms1, SMS)
    assert sms1.sender == '675118923'
    assert sms1.recipient == '721895643'
    assert sms1.message == 'Hi there. Are you ok?'

    assert isinstance(sms1.con, sqlite3.Connection)
    assert isinstance(sms1.cur, sqlite3.Cursor)


def test_send_sms(sms1: SMS, db_con: sqlite3.Connection):
    sms1.send()
    sql = 'SELECT * FROM activity WHERE sender=?'
    result = db_con.cursor().execute(sql, (sms1.sender,))
    row = result.fetchall()
    assert len(row) == 1
    assert row[0]['sender'] == sms1.sender
    assert row[0]['recipient'] == sms1.recipient
    assert row[0]['message'] == sms1.message


def test_sms_representation_as_string(sms1: SMS):
    assert (
        str(sms1)
        == """From: 675118923
To: 721895643
---
Hi there. Are you ok?"""
    )


# --------------
# Tests para SIM
# --------------


def test_build_sim(sim1: SIM):
    assert isinstance(sim1, SIM)
    assert sim1.phone_number == '675118923'
    assert sim1.unlocked is False

    assert isinstance(sim1.con, sqlite3.Connection)
    assert isinstance(sim1.cur, sqlite3.Cursor)


def test_sim_unlock(sim1: SIM):
    sim1.unlock('1167')
    assert sim1.unlocked is True


def test_sim_unlock_fails_when_pin_is_wrong(sim1: SIM):
    sim1.unlock('1111')
    assert sim1.unlocked is False


def test_sim_unlock_fails_when_phone_number_does_not_exist(sim1: SIM):
    sim = SIM('675891118')
    sim.unlock('1111')
    assert sim1.unlocked is False


def test_sim_unlock_works_when_pin_is_wrong_but_puk_is_right(sim1: SIM):
    sim1.unlock('1000', puk='435512')
    assert sim1.unlocked is True


def test_send_sms_from_sim(sim1: SIM, db_con: sqlite3.Connection):
    RECIPIENT = '699123456'
    MESSAGE = 'Python is cool!'

    sim1.unlock('1167')
    sim1.send_sms(recipient=RECIPIENT, message=MESSAGE)

    sql = 'SELECT * FROM activity WHERE recipient=?'
    result = db_con.cursor().execute(sql, (RECIPIENT,))
    rows = result.fetchall()
    assert len(rows) == 1
    assert rows[0]['sender'] == sim1.phone_number
    assert rows[0]['recipient'] == RECIPIENT
    assert rows[0]['message'] == MESSAGE


def test_send_sms_from_sim_fails_when_locked(sim1: SMS, db_con: sqlite3.Connection):
    RECIPIENT = '699123456'
    MESSAGE = 'Python is cool!'

    with pytest.raises(SMSError) as err:
        sim1.send_sms(recipient=RECIPIENT, message=MESSAGE)
    assert str(err.value) == f'SMS "{sim1.phone_number}" is locked!'


def test_send_sms_from_sim_fails_when_invalid_recipient_phone_format(
    sim1: SMS, db_con: sqlite3.Connection
):
    RECIPIENTS = ('699123xyz', '562349774', '781990-12', '-34 699123456', '+34674552313')
    MESSAGE = 'Python is cool!'

    sim1.unlock('1167')
    for recipient in RECIPIENTS:
        with pytest.raises(SMSError) as err:
            sim1.send_sms(recipient=recipient, message=MESSAGE)
        assert str(err.value) == f'Recipient "{recipient}" has invalid phone format!'

    sql = 'SELECT * FROM activity WHERE recipient=?'
    db_cur = db_con.cursor()
    for recipient in RECIPIENTS:
        res = db_cur.execute(sql, (recipient,))
        assert res.fetchone() is None


@pytest.mark.parametrize('recipient', ('+34 678129671', '+51 781328664'))
def test_send_sms_from_sim_works_with_special_recipients(
    sim1: SIM, db_con: sqlite3.Connection, recipient: str
):
    MESSAGE = 'Python is cool!'

    sim1.unlock('1167')
    sim1.send_sms(recipient=recipient, message=MESSAGE)

    sql = 'SELECT * FROM activity WHERE recipient=?'
    result = db_con.cursor().execute(sql, (recipient,))
    rows = result.fetchall()
    assert len(rows) == 1
    assert rows[0]['sender'] == sim1.phone_number
    assert rows[0]['recipient'] == recipient
    assert rows[0]['message'] == MESSAGE


def test_get_sent_sms_from_sim(sim1: SIM, db_con: sqlite3.Connection):
    SMSs = (
        ('675118923', '785638129', 'Message 1'),
        ('675118923', '746663287', 'Message 2'),
        ('675118923', '798994370', 'Message 3'),
        ('675118923', '703428651', 'Message 4'),
    )
    sql = 'INSERT INTO activity(sender, recipient, message) VALUES (?, ?, ?)'
    db_cur = db_con.cursor()
    db_cur.executemany(sql, SMSs)
    db_con.commit()

    sim1.unlock('1167')
    all_sms = sim1.get_sms(sent=True)
    assert isinstance(all_sms, GeneratorType)
    for sms, expected_sms in zip(all_sms, SMSs, strict=True):
        sender, recipient, message = expected_sms
        assert sms.sender == sender
        assert sms.recipient == recipient
        assert sms.message == message


def test_get_received_sms_from_sim(sim1: SIM, db_con: sqlite3.Connection):
    SMSs = (
        ('785638129', '675118923', 'Message 1'),
        ('746663287', '675118923', 'Message 2'),
        ('798994370', '675118923', 'Message 3'),
        ('703428651', '675118923', 'Message 4'),
    )
    sql = 'INSERT INTO activity(sender, recipient, message) VALUES (?, ?, ?)'
    db_cur = db_con.cursor()
    db_cur.executemany(sql, SMSs)
    db_con.commit()

    sim1.unlock('1167')
    all_sms = sim1.get_sms(sent=False)
    assert isinstance(all_sms, GeneratorType)
    for sms, expected_sms in zip(all_sms, SMSs, strict=True):
        sender, recipient, message = expected_sms
        assert sms.sender == sender
        assert sms.recipient == recipient
        assert sms.message == message


# -------------------
# Tests para SMSError
# -------------------


@pytest.mark.parametrize('test_fixture', ('sms1', 'sim1'))
def test_build_mail_error_and_close_connection(test_fixture: str, request: pytest.FixtureRequest):
    """Comprueba que la conexión a la base de datos se cierra
    cuando creamos una excepción propia de tipo SMSError.
    Se comprueba tanto para objetos de tipo SMS como SIM."""
    fixture = request.getfixturevalue(test_fixture)
    SMSError('Houston we have a problem', fixture)
    with pytest.raises(sqlite3.ProgrammingError) as db_err:
        fixture.cur.execute('SELECT * FROM activity')
    assert str(db_err.value) == 'Cannot operate on a closed database.'


@pytest.mark.parametrize('test_fixture', ('sms1', 'sim1'))
def test_build_mail_error_and_repr(test_fixture: str, request: pytest.FixtureRequest):
    """Comprueba que la representación de SMSError coincide
    con el mensaje que le pasamos en el constructor.
    Se comprueba tanto para objetos de tipo SMS como SIM."""
    fixture = request.getfixturevalue(test_fixture)
    err = SMSError('Houston we have a problem', fixture)
    assert str(err) == 'Houston we have a problem'

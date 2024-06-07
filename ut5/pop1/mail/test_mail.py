import sqlite3
from pathlib import Path
from types import GeneratorType

import pytest
from mail import DbHandler, Mail, MailError, MailServer

TEST_DB_PATH = 'test_mail.db'

# **************************************************************
# FIXTURES
# **************************************************************


@pytest.fixture(autouse=True)
def create_test_database():
    db = Path(TEST_DB_PATH)
    db.unlink(missing_ok=True)
    handler = DbHandler(TEST_DB_PATH)
    handler.create_db()
    sql = """INSERT INTO login VALUES("anna", "python", "gmail.com");
INSERT INTO login VALUES("evva", "rust", "icloud.com")"""
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
def mailserver1():
    return MailServer('anna')


@pytest.fixture
def mailserver2():
    return MailServer('evva')


@pytest.fixture
def mailserver3():
    return MailServer('guido')


@pytest.fixture
def mailserver4():
    return MailServer('galindo')


@pytest.fixture
def mail1():
    return Mail(
        sender='vanrossum@python.org',
        recipient='galindo@python.org',
        subject='Hi there',
        body='Are you ok?',
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
        'login': ('username', 'password', 'domain'),
        'activity': ('id', 'sender', 'recipient', 'subject', 'body'),
    }
    assert Path(TEST_DB_PATH).exists()
    cur = db_con.cursor()
    for table, columns in TABLES.items():
        sql = "SELECT ? FROM sqlite_schema WHERE type = 'table'"
        assert cur.execute(sql, [table]).fetchone() is not None
        sql = f"PRAGMA table_info('{table}')"
        for column in columns:
            assert column in [c['name'] for c in cur.execute(sql)]


# ---------------
# Tests para Mail
# ---------------


def test_build_mail(mail1: Mail):
    assert isinstance(mail1, Mail)
    assert mail1.sender == 'vanrossum@python.org'
    assert mail1.recipient == 'galindo@python.org'
    assert mail1.subject == 'Hi there'
    assert mail1.body == 'Are you ok?'

    assert isinstance(mail1.con, sqlite3.Connection)
    assert isinstance(mail1.cur, sqlite3.Cursor)


def test_send_mail(mail1: Mail, db_con: sqlite3.Connection):
    mail1.send()
    sql = 'SELECT * FROM activity WHERE sender="vanrossum@python.org"'
    result = db_con.cursor().execute(sql)
    row = result.fetchall()
    assert len(row) == 1
    assert row[0]['sender'] == 'vanrossum@python.org'
    assert row[0]['recipient'] == 'galindo@python.org'
    assert row[0]['subject'] == 'Hi there'
    assert row[0]['body'] == 'Are you ok?'


def test_mail_representation_as_string(mail1: Mail):
    assert (
        str(mail1)
        == """From: vanrossum@python.org
To: galindo@python.org
---
HI THERE
Are you ok?"""
    )


# ---------------------
# Tests para MailServer
# ---------------------


def test_build_mailserver(mailserver1: MailServer):
    assert isinstance(mailserver1, MailServer)
    assert mailserver1.username == 'anna'
    assert mailserver1.logged is False

    assert isinstance(mailserver1.con, sqlite3.Connection)
    assert isinstance(mailserver1.cur, sqlite3.Cursor)


def test_mailserver_login(mailserver1: MailServer, mailserver2: MailServer):
    mailserver1.login('python')
    assert mailserver1.logged is True
    assert mailserver1.domain == 'gmail.com'

    mailserver2.login('rust')
    assert mailserver2.logged is True
    assert mailserver2.domain == 'icloud.com'


def test_mailserver_login_fails_when_password_is_wrong(
    mailserver1: MailServer, mailserver2: MailServer
):
    mailserver1.login('lisp')
    assert mailserver1.logged is False
    assert mailserver1.domain == ''

    mailserver2.login('java')
    assert mailserver1.logged is False
    assert mailserver1.domain == ''


def test_mailserver_login_fails_when_username_does_not_exist(
    mailserver3: MailServer, mailserver4: MailServer
):
    mailserver3.login('helloworld')
    assert mailserver3.logged is False
    assert mailserver3.domain == ''

    mailserver4.login('helloworld')
    assert mailserver4.logged is False
    assert mailserver4.domain == ''


def test_sender_representation(mailserver1: MailServer, mailserver2: MailServer):
    with pytest.raises(AttributeError):
        assert mailserver1.sender == 'anna@gmail.com'
        assert mailserver2.sender == 'evva@icloud.com'
    mailserver1.login('python')
    assert mailserver1.sender == 'anna@gmail.com'
    mailserver2.login('rust')
    assert mailserver2.sender == 'evva@icloud.com'


def test_send_mail_from_mailserver(mailserver1: MailServer, db_con: sqlite3.Connection):
    RECIPIENT = 'stinner@python.org'
    SUBJECT = 'New Python'
    BODY = 'We are launching a new Python version!'

    mailserver1.login('python')
    mailserver1.send_mail(
        recipient=RECIPIENT,
        subject=SUBJECT,
        body=BODY,
    )
    sql = 'SELECT * FROM activity WHERE recipient=?'
    result = db_con.cursor().execute(sql, (RECIPIENT,))
    rows = result.fetchall()
    assert len(rows) == 1
    assert rows[0]['sender'] == 'anna@gmail.com'
    assert rows[0]['recipient'] == RECIPIENT
    assert rows[0]['subject'] == SUBJECT
    assert rows[0]['body'] == BODY


def test_send_mail_from_mailserver_fails_when_not_logged_in(mailserver1: MailServer):
    RECIPIENT = 'stinner@python.org'
    SUBJECT = 'New Python'
    BODY = 'We are launching a new Python version!'

    with pytest.raises(MailError) as err:
        mailserver1.send_mail(
            recipient=RECIPIENT,
            subject=SUBJECT,
            body=BODY,
        )
    assert str(err.value) == 'User "anna" not logged in!'


def test_send_mail_from_mailserver_fails_when_invalid_recipient_email_format(
    mailserver1: MailServer, db_con: sqlite3.Connection
):
    RECIPIENTS = ('stinner$python.org', 'stinner@python', 'stinner@python&org')
    SUBJECT = 'New Python'
    BODY = 'We are launching a new Python version!'

    mailserver1.login('python')
    for recipient in RECIPIENTS:
        with pytest.raises(MailError) as err:
            mailserver1.send_mail(
                recipient=recipient,
                subject=SUBJECT,
                body=BODY,
            )
        assert str(err.value) == f'Recipient "{recipient}" has invalid mail format!'

    sql = 'SELECT * FROM activity WHERE recipient=?'
    db_cur = db_con.cursor()
    for recipient in RECIPIENTS:
        res = db_cur.execute(sql, (recipient,))
        assert res.fetchone() is None


@pytest.mark.parametrize('recipient', ('info@gov.edu.es', 'main-contact@hello.tech'))
def test_send_mail_from_mailserver_works_with_special_recipients(
    mailserver1: MailServer, db_con: sqlite3.Connection, recipient: str
):
    SUBJECT = 'New Python'
    BODY = 'We are launching a new Python version!'

    mailserver1.login('python')
    mailserver1.send_mail(recipient=recipient, subject=SUBJECT, body=BODY)

    sql = 'SELECT * FROM activity WHERE recipient=?'
    result = db_con.cursor().execute(sql, (recipient,))
    rows = result.fetchall()
    assert len(rows) == 1
    assert rows[0]['sender'] == 'anna@gmail.com'
    assert rows[0]['recipient'] == recipient
    assert rows[0]['subject'] == SUBJECT
    assert rows[0]['body'] == BODY


def test_get_sent_emails_from_mailserver(mailserver1: MailServer, db_con: sqlite3.Connection):
    EMAILS = (
        ('anna@gmail.com', 'core1@python.org', 'Subject1', 'Body1'),
        ('anna@gmail.com', 'core2@python.org', 'Subject2', 'Body2'),
        ('anna@gmail.com', 'core3@python.org', 'Subject3', 'Body3'),
        ('anna@gmail.com', 'core4@python.org', 'Subject4', 'Body4'),
    )
    sql = 'INSERT INTO activity(sender, recipient, subject, body) VALUES (?, ?, ?, ?)'
    db_cur = db_con.cursor()
    db_cur.executemany(sql, EMAILS)
    db_con.commit()

    mailserver1.login('python')
    emails = mailserver1.get_emails(sent=True)
    assert isinstance(emails, GeneratorType)
    for email, expected_email in zip(emails, EMAILS, strict=True):
        sender, recipient, subject, body = expected_email
        assert email.sender == sender
        assert email.recipient == recipient
        assert email.subject == subject
        assert email.body == body


def test_get_received_emails_from_mailserver(mailserver1: MailServer, db_con: sqlite3.Connection):
    EMAILS = (
        ('core1@python.org', 'anna@gmail.com', 'Subject1', 'Body1'),
        ('core2@python.org', 'anna@gmail.com', 'Subject2', 'Body2'),
        ('core3@python.org', 'anna@gmail.com', 'Subject3', 'Body3'),
        ('core4@python.org', 'anna@gmail.com', 'Subject4', 'Body4'),
    )
    sql = 'INSERT INTO activity(sender, recipient, subject, body) VALUES (?, ?, ?, ?)'
    db_cur = db_con.cursor()
    db_cur.executemany(sql, EMAILS)
    db_con.commit()

    mailserver1.login('python')
    emails = mailserver1.get_emails(sent=False)
    assert isinstance(emails, GeneratorType)
    for email, expected_email in zip(emails, EMAILS, strict=True):
        sender, recipient, subject, body = expected_email
        assert email.sender == sender
        assert email.recipient == recipient
        assert email.subject == subject
        assert email.body == body


# --------------------
# Tests para MailError
# --------------------


@pytest.mark.parametrize('mail_fixture', ('mail1', 'mailserver1'))
def test_build_mail_error_and_close_connection(mail_fixture: str, request: pytest.FixtureRequest):
    mail = request.getfixturevalue(mail_fixture)
    MailError('Houston we have a problem', mail)
    with pytest.raises(sqlite3.ProgrammingError) as db_err:
        mail.cur.execute('SELECT * FROM activity')
    assert str(db_err.value) == 'Cannot operate on a closed database.'


@pytest.mark.parametrize('mail_fixture', ('mail1', 'mailserver1'))
def test_build_mail_error_and_repr(mail_fixture: str, request: pytest.FixtureRequest):
    mail = request.getfixturevalue(mail_fixture)
    err = MailError('Houston we have a problem', mail)
    assert str(err) == 'Houston we have a problem'

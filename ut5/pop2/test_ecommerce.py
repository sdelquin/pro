import sqlite3
from pathlib import Path

import create_db
import ecommerce
import pytest
from ecommerce import Cart, Product, User

TEST_DB_PATH = 'ecommerce.db'

# **************************************************************
# FIXTURES
# **************************************************************


@pytest.fixture(autouse=True)
def create_test_database():
    try:
        create_db.create(TEST_DB_PATH)
        yield
    except Exception as err:
        raise err
    finally:
        Path(TEST_DB_PATH).unlink(missing_ok=True)


@pytest.fixture()
def dbcon():
    con = sqlite3.connect(TEST_DB_PATH)
    con.row_factory = sqlite3.Row
    yield con
    con.close()


@pytest.fixture(autouse=True)
def make_db_attrs_use_test_database(monkeypatch: pytest.MonkeyPatch):
    for class_ in (User, Product, Cart):
        monkeypatch.setattr(class_, 'con', sqlite3.connect(TEST_DB_PATH))
        monkeypatch.setattr(class_.con, 'row_factory', sqlite3.Row)  # type: ignore
        monkeypatch.setattr(class_, 'cur', class_.con.cursor())  # type: ignore


USER1_USERNAME = 'scrowww01'
USER1_NAME = 'Sheryl'
USER1_SURNAME = 'Crow'


@pytest.fixture
def user1():
    return User(USER1_USERNAME, USER1_NAME, USER1_SURNAME)


USER2_USERNAME = 'sspiteri7'
USER2_NAME = 'Sharleen'
USER2_SURNAME = 'Spiteri'


@pytest.fixture
def user2():
    return User(USER2_USERNAME, USER2_NAME, USER2_SURNAME)


PRODUCT1_NAME = 'Gunde'
PRODUCT1_STOCK = 15
PRODUCT1_PRICE = 12.5


@pytest.fixture
def product1():
    return Product(PRODUCT1_NAME, PRODUCT1_STOCK, PRODUCT1_PRICE)


PRODUCT2_NAME = 'Lisabo'
PRODUCT2_STOCK = 21
PRODUCT2_PRICE = 30.75


@pytest.fixture
def product2():
    return Product(PRODUCT2_NAME, PRODUCT2_STOCK, PRODUCT2_PRICE)


PRODUCT3_NAME = 'Adde'
PRODUCT3_STOCK = 45
PRODUCT3_PRICE = 14.25


@pytest.fixture
def product3():
    return Product(PRODUCT3_NAME, PRODUCT3_STOCK, PRODUCT3_PRICE)


# ************************************************************
# Tests -> User
# ************************************************************


def test_skeleton_is_correct():
    assert getattr(ecommerce, 'DB_PATH', None) == TEST_DB_PATH
    assert getattr(ecommerce, 'User', None) is not None
    assert getattr(ecommerce, 'Product', None) is not None
    assert getattr(ecommerce, 'Cart', None) is not None


def test_build_user(user1: User, dbcon: sqlite3.Connection):
    assert user1.username == USER1_USERNAME
    assert user1.name == USER1_NAME
    assert user1.surname == USER1_SURNAME
    assert user1.id is None

    res = dbcon.cursor().execute('SELECT COUNT(*) FROM user')
    assert res.fetchone()[0] == 0

    user = User(USER1_USERNAME, USER1_NAME, USER1_SURNAME, 1)
    assert user.username == USER1_USERNAME
    assert user.name == USER1_NAME
    assert user.surname == USER1_SURNAME
    assert user.id == 1

    res = dbcon.execute('SELECT COUNT(*) FROM user')
    assert res.fetchone()[0] == 0


def test_build_user_fails_when_name_is_incorrect():
    for username in ('bruce', '4bruce001', 'bruce743z', 'bruce:R9', 'Bruce87692'):
        with pytest.raises(ValueError) as err:
            User(username, '', '')
        assert str(err.value) == f'User "{username}" does not follow security rules!'


def test_save_user(user1: User, dbcon: sqlite3.Connection):
    res = dbcon.cursor().execute('SELECT COUNT(*) FROM user WHERE username=?', (USER1_USERNAME,))
    assert res.fetchone()[0] == 0

    user1.save()

    res = dbcon.cursor().execute('SELECT * FROM user WHERE username=?', (USER1_USERNAME,))
    row = res.fetchone()
    assert row['username'] == user1.username
    assert row['name'] == user1.name
    assert row['surname'] == user1.surname
    assert row['id'] == 1

    with pytest.raises(sqlite3.IntegrityError) as err:
        user1.save()
    assert str(err.value) == 'UNIQUE constraint failed: user.username'


def test_update_user(user1: User, user2: User, dbcon: sqlite3.Connection):
    with pytest.raises(ValueError) as err:
        user1.update()
    assert str(err.value) == f'User "{USER1_USERNAME}" has not been yet saved into DB!'

    user1.save()

    res = dbcon.cursor().execute('SELECT * FROM user WHERE username=?', (USER1_USERNAME,))
    row = res.fetchone()
    assert row['username'] == user1.username
    assert row['name'] == user1.name
    assert row['surname'] == user1.surname
    assert row['id'] == 1

    user1.name = user2.name
    user1.surname = user2.surname
    user1.update()

    res = dbcon.cursor().execute('SELECT * FROM user WHERE username=?', (USER1_USERNAME,))
    row = res.fetchone()
    assert row['name'] == user1.name
    assert row['surname'] == user1.surname
    assert row['id'] == 1


def test_user_representation(user1: User, user2: User):
    assert str(user1) == 'Sheryl Crow'
    assert str(user2) == 'Sharleen Spiteri'


def test_products_are_equal(product1: Product, product2: Product):
    product3 = product1
    product3.name = PRODUCT1_NAME
    assert product1 == product3

    assert product1 != product2
    assert product1 != 'product1'


def test_build_user_from_id(user1: User, dbcon: sqlite3.Connection):
    dbcur = dbcon.cursor()
    dbcur.execute(
        'INSERT INTO user (username, name, surname) VALUES (?, ?, ?)',
        (user1.username, user1.name, user1.surname),
    )
    dbcon.commit()
    user_id = dbcur.lastrowid

    built_user = User.from_id(user_id)  # type: ignore
    assert isinstance(built_user, User)
    assert built_user.username == user1.username
    assert built_user.name == user1.name
    assert built_user.surname == user1.surname
    assert built_user.id is not None


def test_build_user_from_id_fails_when_product_id_does_not_exist():
    with pytest.raises(ValueError) as err:
        User.from_id(0)
    assert str(err.value) == 'User with id 0 does not exist in DB!'


# ************************************************************
# Tests -> Product
# ************************************************************


def test_build_product(product1: Product, dbcon: sqlite3.Connection):
    assert product1.name == PRODUCT1_NAME
    assert product1.stock == PRODUCT1_STOCK
    assert product1.price == PRODUCT1_PRICE
    assert product1.id is None

    res = dbcon.cursor().execute('SELECT COUNT(*) FROM product')
    assert res.fetchone()[0] == 0

    product = Product(PRODUCT1_NAME, PRODUCT1_STOCK, PRODUCT1_PRICE, 1)
    assert product.name == PRODUCT1_NAME
    assert product.stock == PRODUCT1_STOCK
    assert product.price == PRODUCT1_PRICE
    assert product.id == 1

    res = dbcon.execute('SELECT COUNT(*) FROM product')
    assert res.fetchone()[0] == 0


def test_save_product(product1: Product, dbcon: sqlite3.Connection):
    res = dbcon.cursor().execute('SELECT COUNT(*) FROM product WHERE name=?', (product1.name,))
    assert res.fetchone()[0] == 0

    product1.save()

    res = dbcon.cursor().execute('SELECT * FROM product WHERE name=?', (product1.name,))
    row = res.fetchone()
    assert row['name'] == product1.name
    assert row['stock'] == product1.stock
    assert row['price'] == product1.price
    assert row['id'] == 1

    with pytest.raises(sqlite3.IntegrityError) as err:
        product1.save()
    assert str(err.value) == 'UNIQUE constraint failed: product.name'


def test_update_product(product1: Product, product2: Product, dbcon: sqlite3.Connection):
    with pytest.raises(ValueError) as err:
        product1.update()
    assert str(err.value) == f'Product "{PRODUCT1_NAME}" has not been yet saved into DB!'

    product1.save()

    res = dbcon.cursor().execute('SELECT * FROM product WHERE name=?', (PRODUCT1_NAME,))
    row = res.fetchone()
    assert row['name'] == product1.name
    assert row['stock'] == product1.stock
    assert row['price'] == product1.price
    assert row['id'] == 1

    product1.stock = product2.stock
    product1.price = product2.price
    product1.update()

    res = dbcon.cursor().execute('SELECT * FROM product WHERE name=?', (PRODUCT1_NAME,))
    row = res.fetchone()
    assert row['name'] == product1.name
    assert row['stock'] == product1.stock
    assert row['price'] == product1.price
    assert row['id'] == 1


def test_sell_product(product1: Product, dbcon: sqlite3.Connection):
    sql = 'INSERT INTO product (name, stock, price) VALUES (?, ?, ?)'
    dbcur = dbcon.cursor()
    dbcur.execute(sql, (product1.name, product1.stock, product1.price))
    dbcon.commit()
    product1.id = dbcur.lastrowid

    product1.sell(10)

    assert product1.stock == 5

    sql = 'SELECT * FROM product WHERE id=?'
    res = dbcur.execute(sql, (product1.id,))
    row = res.fetchone()
    assert row['stock'] == 5


def test_restock_product(product1: Product, dbcon: sqlite3.Connection):
    sql = 'INSERT INTO product (name, stock, price) VALUES (?, ?, ?)'
    dbcur = dbcon.cursor()
    dbcur.execute(sql, (product1.name, product1.stock, product1.price))
    dbcon.commit()
    product1.id = dbcur.lastrowid

    product1.restock(10)

    assert product1.stock == 25

    sql = 'SELECT * FROM product WHERE id=?'
    res = dbcur.execute(sql, (product1.id,))
    row = res.fetchone()
    assert row['stock'] == 25


def test_sell_product_fails_when_not_enough_stock(product1: Product, dbcon: sqlite3.Connection):
    sql = 'INSERT INTO product (name, stock, price) VALUES (?, ?, ?)'
    dbcur = dbcon.cursor()
    dbcur.execute(sql, (product1.name, product1.stock, product1.price))
    dbcon.commit()
    product1.id = dbcur.lastrowid

    with pytest.raises(ValueError) as err:
        product1.sell(20)
    assert str(err.value) == f'Not enough stock for product "{product1.name}"!'

    sql = 'SELECT * FROM product WHERE id=?'
    res = dbcur.execute(sql, (product1.id,))
    row = res.fetchone()
    assert row['stock'] == PRODUCT1_STOCK


def test_product_representation(product1: Product, product2: Product):
    assert str(product1) == PRODUCT1_NAME
    assert str(product2) == PRODUCT2_NAME


def test_build_product_from_id(product1: Product, dbcon: sqlite3.Connection):
    dbcur = dbcon.cursor()
    dbcur.execute(
        'INSERT INTO product (name, stock, price) VALUES (?, ?, ?)',
        (product1.name, product1.stock, product1.price),
    )
    dbcon.commit()
    product_id = dbcur.lastrowid

    built_product = Product.from_id(product_id)  # type: ignore
    assert isinstance(built_product, Product)
    assert built_product.name == product1.name
    assert built_product.stock == product1.stock
    assert built_product.price == product1.price
    assert built_product.id is not None


def test_build_product_from_id_fails_when_product_id_does_not_exist():
    with pytest.raises(ValueError) as err:
        Product.from_id(0)
    assert str(err.value) == 'Product with id 0 does not exist in DB!'


# ************************************************************
# Tests -> Cart
# ************************************************************


def test_purchase(user1: User, product1: Product, dbcon: sqlite3.Connection):
    dbcur = dbcon.cursor()

    sql = 'INSERT INTO user (username, name, surname) VALUES (?, ?, ?)'
    dbcur.execute(sql, (user1.username, user1.name, user1.surname))
    dbcon.commit()
    user1.id = dbcur.lastrowid

    sql = 'INSERT INTO product (name, stock, price) VALUES (?, ?, ?)'
    dbcur.execute(sql, (product1.name, product1.stock, product1.price))
    dbcon.commit()
    product1.id = dbcur.lastrowid

    Cart.purchase(1, 1, 5)

    sql = 'SELECT * FROM cart WHERE user_id=? AND product_id=?'
    res = dbcur.execute(sql, (user1.id, product1.id))
    row = res.fetchone()
    assert row['qty'] == 5


def test_clean_cart(
    user1: User, product1: Product, product2: Product, product3: Product, dbcon: sqlite3.Connection
):
    dbcur = dbcon.cursor()

    sql = 'INSERT INTO user (username, name, surname) VALUES (?, ?, ?)'
    dbcur.execute(sql, (user1.username, user1.name, user1.surname))
    dbcon.commit()
    user1.id = dbcur.lastrowid

    sql = 'INSERT INTO product (name, stock, price) VALUES (?, ?, ?)'
    dbcur.execute(sql, (product1.name, product1.stock, product1.price))
    dbcon.commit()
    product1.id = dbcur.lastrowid

    sql = 'INSERT INTO product (name, stock, price) VALUES (?, ?, ?)'
    dbcur.execute(sql, (product2.name, product2.stock, product2.price))
    dbcon.commit()
    product2.id = dbcur.lastrowid

    sql = 'INSERT INTO product (name, stock, price) VALUES (?, ?, ?)'
    dbcur.execute(sql, (product3.name, product3.stock, product3.price))
    dbcon.commit()
    product3.id = dbcur.lastrowid

    sql = 'INSERT INTO cart (user_id, product_id, qty) VALUES (?, ?, ?)'
    dbcur.execute(sql, (user1.id, product1.id, 4))
    dbcon.commit()

    sql = 'INSERT INTO cart (user_id, product_id, qty) VALUES (?, ?, ?)'
    dbcur.execute(sql, (user1.id, product2.id, 6))
    dbcon.commit()

    Cart.clean(user1.id)

    sql = 'SELECT * FROM product WHERE id=?'
    res = dbcur.execute(sql, (product1.id,))
    row = res.fetchone()
    assert row['stock'] == PRODUCT1_STOCK + 4

    sql = 'SELECT * FROM product WHERE id=?'
    res = dbcur.execute(sql, (product2.id,))
    row = res.fetchone()
    assert row['stock'] == PRODUCT2_STOCK + 6

    sql = 'SELECT * FROM cart WHERE user_id=?'
    assert dbcur.execute(sql, (user1.id,)).fetchone() is None

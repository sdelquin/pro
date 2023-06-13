import sqlite3
from pathlib import Path


def create(db_path: str):
    db = Path(db_path)
    db.unlink(missing_ok=True)

    con = sqlite3.connect(db)
    cur = con.cursor()

    sql = '''
    CREATE TABLE user (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE,
        name TEXT,
        surname TEXT
    );

    CREATE TABLE product (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE,
        stock INTEGER,
        price REAL
    );

    CREATE TABLE cart (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        product_id INTEGER,
        qty INTEGER,
        FOREIGN KEY (user_id) REFERENCES user(id),
        FOREIGN KEY (product_id) REFERENCES product(id)
    );
    '''

    cur.executescript(sql)
    con.commit()
    con.close()


if __name__ == '__main__':
    create('ecommerce.db')

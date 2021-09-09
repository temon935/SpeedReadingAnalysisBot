import sqlite3


__connection = None


def get_connection():
    global __connection
    if __connection is None:
        __connection = sqlite3.connect('libdb.db')
    return __connection


def init_db(force: bool = False):
    conn = get_connection()

    c = conn.cursor()

    if force:
        c.execute('DROP TABLE IF EXIST user_book')

    c.execute('''
        CREATE TABLE IF NOT EXIST user_book (
            book_id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            num_of_page INTEGER NOT NULL,
            words_on_page INTEGER NOT NULL,
            image )    
    ''')

    conn.commit()


def add_message():
    pass
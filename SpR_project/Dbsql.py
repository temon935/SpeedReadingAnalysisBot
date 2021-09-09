import sqlite3


conn = sqlite3.connect('books.db')
cur = conn.cursor()
'''cur.execute("""CREATE TABLE IF NOT EXISTS users(
   user_id INT PRIMARY KEY,
   books_list_id INT,
   chat_id INT);
""")
conn.commit()
cur.execute("""CREATE TABLE IF NOT EXISTS books(
   book_id INT,
   books_list_id INT,
   title TEXT,
   number_of_pages TEXT,
   number_of_words TEXT,
   book_cover TEXT,
   FOREIGN KEY (books_list_id) references users(books_list_id));
""")
conn.commit()
cur.execute("""CREATE TABLE IF NOT EXISTS CUROPN(
   cur_opn_id INT PRIMARY KEY,
   book_id INT,
   cur_time_opn TEXT,
   cur_time_cls TEXT,
   page_cls INT,
   cur_speed INT,
   FOREIGN KEY (book_id) references books(book_id));
""")
conn.commit()

user = ('1', '1', '123411')
cur.execute("INSERT INTO users VALUES(?, ?, ?);", user)
conn.commit()

book1 = ('1', '1', 'Властелин колец', '1080', '101', 'https://kinogovno1.com')
book2 = ('2', '1', 'Точка обмана', '1300', '120', 'https://kinogovno2.com')
book3 = ('3', '1', 'Sapiens. Краткая история человечества', '857', '90', 'https://kinogovno3.com')
book4 = ('4', '1', 'Зачем мы спим', '677', '101', 'https://kinogovno4.com')
cur.execute("INSERT INTO books VALUES(?, ?, ?, ?, ?, ?);", book1)
conn.commit()
cur.execute("INSERT INTO books VALUES(?, ?, ?, ?, ?, ?);", book2)
conn.commit()
cur.execute("INSERT INTO books VALUES(?, ?, ?, ?, ?, ?);", book3)
conn.commit()
cur.execute("INSERT INTO books VALUES(?, ?, ?, ?, ?, ?);", book4)
conn.commit()

opn1 = ('1', '1', '2021-08-14 17:01:20', '2021-08-14 19:21:20', '24', '344')
opn2 = ('2', '1', '2021-08-15 17:01:20', '2021-08-14 19:01:20', '48', '368')
opn3 = ('3', '1', '2021-08-16 17:01:20', '2021-08-14 19:00:20', '72', '370')
cur.execute("INSERT INTO CUROPN VALUES(?, ?, ?, ?, ?, ?);", opn1)
conn.commit()
cur.execute("INSERT INTO CUROPN VALUES(?, ?, ?, ?, ?, ?);", opn2)
conn.commit()
cur.execute("INSERT INTO CUROPN VALUES(?, ?, ?, ?, ?, ?);", opn3)
conn.commit()'''

cur.execute("SELECT user_id, title, cur_speed "
            "FROM books inner join users on books.books_list_id = users.books_list_id "
            "join CUROPN on books.book_id = curopn.book_id "
            "WHERE curopn.cur_speed > 350;")
result = cur.fetchall()
print(result)
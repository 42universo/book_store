import sqlite3
from sqlite3 import Error

class BookStore():
    def __init__(self,path):
        self.con = self.connect(path)

    def connect(self,path):
        try:
            con = sqlite3.connect(path)
            print('Connected to DB')
            return con
        except Error as e:
            print(e)

    def create_table(self):
        try:
            with self.con:
                cursor = self.con.cursor()
                cursor.execute('''CREATE TABLE book_store(
                name text,
                description text,
                price real,
                rate real);''')
                print('Created table')
        except Error as e:
            print(e)

    def delete_book(self, name):
        try:
            with self.con:
                cursor = self.con.cursor()
                cursor.execute(f'DELETE FROM book_store WHERE name="{name}"')
                print('Book deleted')
        except Error as e:
            print(e)

    def insert_book(self, name, description, price, rate):
        try:
            with self.con:
                cursor = self.con.cursor()
                cursor.execute(f'''INSERT INTO book_store(name, description, price, rate)
                VALUES("{name}","{description}",{price},{rate})''')
                print('Book added')
        except Error as e:
            print(e)

    def select_all(self):
        try:
            with self.con:
                cursor = self.con.cursor()
                cursor.execute('SELECT * FROM book_store')
                return cursor.fetchall()
        except Error as e:
            print(e)
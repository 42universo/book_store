import tkinter as tk
from tkinter import messagebox
from database import BookStore

db = BookStore(':memory:')
db.create_table()
db.insert_book('Harry Potter', 'About wizards', 30.50, 4.5)
db.insert_book('Alice in the wonderland', 'Crazy world', 20.30, 4)
db.insert_book('Romeo and Juliet', 'Romance between enemies',25, 4.2)
db.insert_book('Diary of Anne Frank', 'Real story, about nazi time', 23.50, 4.2)
books = db.select_all()

def create_table_frame():
    global table
    table = tk.Frame(master=main_frame)
    table.columnconfigure([0, 1, 2, 3], weight=1)
    table.grid(column=0, row=1, sticky='nsew')
    name_c = tk.Label(text='NAME', master=table)
    name_c.grid(column=0, row=0, sticky='ew')
    description_c = tk.Label(text='DESCRIPTION', master=table)
    description_c.grid(column=1, row=0, sticky='ew')
    price_c = tk.Label(text='PRICE', master=table)
    price_c.grid(column=2, row=0, sticky='ew')
    rate_c = tk.Label(text='RATE', master=table)
    rate_c.grid(column=3, row=0, sticky='ew')
    r = 1
    for book in books:
        name = tk.Label(text=book[0], master=table)
        name.grid(column=0, row=r, sticky='ew')

        description = tk.Label(text=book[1], master=table)
        description.grid(column=1, row=r, sticky='ew')

        price = tk.Label(text=book[2], master=table)
        price.grid(column=2, row=r, sticky='ew')

        rate = tk.Label(text=book[3], master=table)
        rate.grid(column=3, row=r, sticky='ew')
        r += 1

def buy_book():
    name = input.get()
    try:
        db.delete_book(name)
        messagebox.showinfo(message=f'Book {name} was bought')
        global books
        books = db.select_all()
        table.destroy()
        create_table_frame()
    except:
        messagebox.showinfo(message=f'Book {name} not found')

window = tk.Tk()
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

main_frame = tk.Frame()
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure([0,1,2,3], weight=1)
main_frame.grid(column=0, row=0, sticky='nsew')

title = tk.Label(text='Book Store', master=main_frame)
title.grid(column=0, row=0, sticky='ew', pady=30)

create_table_frame()


input = tk.Entry(master=main_frame, width=35)
input.grid(column=0, row=2, pady=8)

buy_btn = tk.Button(text='Buy!!', master=main_frame, command=buy_book)
buy_btn.grid(column=0, row=3)

window.mainloop()
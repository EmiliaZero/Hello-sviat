import tkinter as tk
import tkinter.messagebox
import sqlite3

default_accounts = {"Sviat": "sviatpass1234",
                    "Admin": "adminPass2@30",
                    "Guest": "guestpass"}
try:
    open("users.sl3", "r")
    connection = sqlite3.connect("users.sl3", 5)
    cur = connection.cursor()
    cur.execute("SELECT rowid, login, password FROM accounts;")
    res = cur.fetchall()
    print(res)
except FileNotFoundError:
    open("users.sl3", "w")
    connection = sqlite3.connect("users.sl3", 5)
    cur = connection.cursor()
    cur.execute("CREATE TABLE accounts (login TEXT, password TEXT);")
    connection.commit()
    cur.execute("CREATE TABLE prod (name TEXT, price TEXT, number TEXT);")
    connection.commit()
    for person in range(0, len(default_accounts)):
        cur.execute(
            f"INSERT INTO accounts (login, password) VALUES ('{list(default_accounts.keys())[person]}', '{list(default_accounts.values())[person]}');")
        connection.commit()
    cur.execute("SELECT rowid, login, password FROM accounts;")
    res = cur.fetchall()
    print(res)

items = []


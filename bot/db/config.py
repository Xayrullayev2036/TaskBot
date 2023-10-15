import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

conn = sqlite3.connect('/home/diyorbek/PycharmProjects/Modul8/TaskBot/tg_bot')
cursor = conn.cursor()


# cursor.execute('''CREATE TABLE  IF NOT EXISTS users
#                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                   name TEXT NOT NULL,
#                   user_id TEXT NOT NULL,
#                   data TEXT NOT NULL,
#                   phone_number TEXT NOT NULL,
#                   latitude TEXT NOT NULL,
#                   longitude TEXT NOT NULL,
#                   status TEXT NOT NULL)''')


def save_database(data):
    conn = sqlite3.connect('/home/diyorbek/PycharmProjects/Modul8/TaskBot/tg_bot')
    cursor.execute(
        "INSERT INTO users (name,user_id,data,phone_number,latitude,longitude,status) VALUES (?,?,?,?,?,?,?)",
        (data["name"], data["user_id"], data["data"], data["phone"], data["latitude"], data["longitude"],
         data["status"]))
    conn.commit()
    conn.close()

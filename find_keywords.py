import requests
import sqlite3
import datetime
import time
import os
from dotenv import load_dotenv

load_dotenv()



def send_telegram_message(i,name_group):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    db = sqlite3.connect('server.db')
    sql = db.cursor()

    def execute_read_query(sql, query):
        cursor = sql
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")

    select_users = "SELECT id_users FROM id_of_users"
    users = execute_read_query(sql, select_users)
    token = os.getenv('token')
    for user in users:
        token = os.getenv('token')
        url = f'https://api.telegram.org/bot{token}/sendMessage'
        responce_name_group = requests.post(url=url, data={'chat_id': user, 'text': name_group, })
        responce = requests.post(url=url, data={'chat_id': user, 'text': i, })
        print(responce_name_group, responce)

def key_words(name_group):
    db = sqlite3.connect('server.db')
    sql = db.cursor()

    sql.execute("""CREATE TABLE IF NOT EXISTS chat_of_reels(
        id  INTEGER PRIMARY KEY AUTOINCREMENT,
        name_of_chat TEXT,
        message TEXT,
        date DATE
    )""")
    print('Подключились к базе данных')

    sql.execute(
        "SELECT message, name_of_chat FROM messages_of_chats WHERE (name_of_chat LIKE ?) AND  (message LIKE '%reels%' or message LIKE '%рилс%' or message LIKE '%youtube%' or message LIKE '%рилз%' or message LIKE '%tiktok%')",([name_group]))
    results = sql.fetchall()
    count1=0
    for i in results:
        info = sql.execute('SELECT message, name_of_chat FROM chat_of_reels WHERE message=? AND name_of_chat=?', (str(i),name_group))
        if info.fetchone() is None:
            date = datetime.datetime.now()
            sql.execute("""INSERT INTO chat_of_reels (id ,name_of_chat, message,date) VALUES (NULL,?,?,?)""",(name_group, str(i),date))
            send_telegram_message(i,name_group)
            db.commit()
        else:
            pass
    if count1==0:
        print('Нет новых сообщений')
    sql.close()
    db.close()

key_words('МИР КРЕАТОРОВ')
time.sleep(30)
key_words('Find a Job Abroad LinkedIn')
time.sleep(30)
key_words('Точно продюсеры')
time.sleep(30)
key_words('Реальный запуск')
time.sleep(30)
key_words('Startup never sleeps')






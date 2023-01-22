from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
import sqlite3
from telegram_bot import api_id_user, api_hash_user, phone_user
import datetime
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty


def parser(name_group):

    # создаем базу данных
    db = sqlite3.connect('server.db')
    sql = db.cursor()

    sql.execute("CREATE TABLE IF NOT EXISTS messages_of_chats(id INTEGER PRIMARY KEY AUTOINCREMENT,name_of_chat TEXT,message TEXT,date DATE)")

    # Обязательно подключить к Telegram API
    api_id = api_id_user
    api_hash = api_hash_user
    phone = phone_user

    client = TelegramClient(phone, api_id, api_hash)
    client.start()


    chats = []
    last_date = None
    size_chats = 200
    groups = []
    result = client(GetDialogsRequest(
        offset_date=last_date,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=size_chats,
        hash=0
    ))

    chats.extend(result.chats)

    for chat in chats:
        try:
            if chat.megagroup == True:
                groups.append(chat)
        except:
            continue

    for g in chats:
        if g.title ==name_group:
            print(g)
            target_group= g



    #Переменные для GetHistoryRequest
    all_messages=[]
    offset_id = 0
    limit = 1000
    total_messages = 0
    total_count_limit = 1000
    print(f'Начинаю сканирование чата "{name_group}"')

    while True:
        history = client(GetHistoryRequest(
            peer=name_group,
            offset_id=offset_id,
            offset_date=None,
            add_offset=0,
            limit=limit,
            max_id=0,
            min_id=0,
            hash=0
        ))
        if not history.messages:
            break
        messages = history.messages
        for message in messages:
            total_messages += 1
            all_messages.append(message.message)
        # Добавим параметр message к методу message.
        offset_id = messages[len(messages) - 1].id
        if total_count_limit != 0 and total_messages >= total_count_limit:
            break
    print("Сохраняем сообщения в базу данных..")  # Cообщение для пользователя о том, что начался парсинг сообщений.

    #Добавляем сообщения в базу данных
    count1 = 0
    for i in all_messages:
        info = sql.execute(f'SELECT message FROM messages_of_chats WHERE message=?', (i,))
        if info.fetchone() is None:
            x = datetime.datetime.now()
            count1+=1
            sql.execute(f"""INSERT INTO messages_of_chats (id ,name_of_chat, message,date) VALUES (NULL,?,?,?)""",(name_group,i,x))
            db.commit()
        else:
            pass

    sql.close()
    db.close()


    print("Парсинг сообщений группы успешно выполнен.")

    client.disconnect()


parser('Find a Job Abroad LinkedIn')
parser('МИР КРЕАТОРОВ')
parser('Точно продюсеры')
parser('Реальный запуск')
parser('Startup never sleeps')
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import PeerChannel
from telethon.tl.custom import Message
import csv
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import time

from telegram_bot import api_id_user, api_hash_user, phone_user
def parser():
    # Обязательно подключить к Telegram API
    api_id = api_id_user
    api_hash = api_hash_user
    phone = phone_user

    client = TelegramClient(phone, api_id, api_hash)
    client.start()



    #Показываем чаты и группы
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
        if g.title =='МИР КРЕАТОРОВ':
            print(g)
            target_group= g

    '''print('Выберите номер группы из перечня:')
    i = 0
    for g in chats:
        print(str(i) + '-' + g.title)
        i += 1
    g_index = input("Введите нужную цифру:")
    target_group = chats[int(g_index)]'''



    '''
    print('Узнаем пользователей...')
    all_participants = []
    all_participants = client.get_participants(target_group)
    
    print('Сохраняем данные в файл...')
    with open("members.csv", "w", encoding='UTF-8') as f:
        writer = csv.writer(f, delimiter=',', lineterminator="\n")
        writer.writerow(['username', 'name', 'group'])
        for user in all_participants:
            if user.username:
                username = user.username
            else:
                username = ""
            if user.first_name:
                first_name = user.first_name
            else:
                first_name = ""
            if user.last_name:
                last_name = user.last_name
            else:
                last_name = ""
            name = (first_name + ' ' + last_name).strip()
            writer.writerow([username, name, target_group.title])
            
    print('Парсинг участников группы успешно выполнен.')
    '''
    #Парсинг сообщений
    all_messages=[]
    offset_id = 0
    limit = 100
    total_messages = 0
    total_count_limit = 1000
    print('Начинаю сканирование...')

    while True:
        history = client(GetHistoryRequest(
            peer=target_group,
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
        x = []
        for message in messages:
            total_messages += 1
            all_messages.append(message.message)
        # Добавим параметр message к методу message.
        offset_id = messages[len(messages) - 1].id
        if total_count_limit != 0 and total_messages >= total_count_limit:
            break
    print(all_messages)
    print("Сохраняем данные в файл...")  # Cообщение для пользователя о том, что начался парсинг сообщений.






    with open("chats.csv", "w", encoding="UTF-8") as f:
        writer = csv.writer(f, delimiter=",", lineterminator="\n")
        writer.writerow(["message"])
        for message in all_messages:
           writer.writerow([message])

    print("Парсинг сообщений группы успешно выполнен.")
    client.disconnect()
while True:
    parser()
    time.sleep(86400)


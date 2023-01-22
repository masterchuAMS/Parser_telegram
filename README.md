# Parser_telegram
## Бот Parser_telegram
Бот, который парсит чаты в телеграме по ключевым словам и отправляет пользователю.

## Проблема

Я нахожусь в чатах и не хочу пропускать сообщения по работе (создание рилсов и шортсов) Бывает, что в одном чате по 1000 сообщений за день и невозможно отследить нужные. Можно, конечно, ручками вбивать ключевые слова по поиску, но это можно автоматизировать с помощью бота.



## Решение

Я использовал библиотеки telethon, telebot, request чтобы связываться с Telegram API. Для хранения сообщений использовал базу данных sqlite3.
На это участке кода показываю как работает метод GetHistoryRequest, который передает историю чата, которую можно спарсить. 

```python 
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
```
У меня 3 исполняемых файла: Hello_file, main, find_keywords. Hello_file отвечает за приветствие пользователя и запоминание его id. Main - основной файл на telethon, который подключается к Telegram API, парсит сообщения, создает базу данных.
find_keywords запускает скрипт на SQL, чтобы найти ключевые сообщения и отправляет через request сообщение пользователю через бот. 


## Детали
- Чтобы можно было отправлять всем пользователям сообщения, я использовал handler /start из библиотеки telebot, чтобы запомнить пользователя id.Без него бот не отправляет сообщения из базы данных  
- Чтобы ускорить код, добавлял больше команд SQL, а не Python.
- Метод GetHistoryRequest не будет работать, если не прописать атрибуты, как у меня в примере. 
- Можно парсить только чаты, в которых вы сами сидите.

# Установка
## Требования 
- Python 3.6
- Linux/Windows/Mac/

## Как установить 
Запускаете команды в терминале:
```bash
cd ~/Downloads  # or anywhere else
git clone https://github.com/masterchuAMS/Parser_telegram
cd Parser_telegram
pip install .
```
Обязательно нужно подключиться в Telegram API, получить token и api.

## Как настраивать
Я пока не сделал отдельного файла config. Надо лезть в код и самому изменять. 


## Как запустить
Запускаете Hello_file, он приветсвует и сохраняет ID, файл должен работать постоянно. Затем запускате файл main.py, он спарсит чаты, которые вам интересны. Потом запускаете файл find keywords, он отфильтрует, найдет сообщения и отправит пользователю бота. 





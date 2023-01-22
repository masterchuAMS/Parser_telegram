import telebot
import sqlite3
from telegram_bot import token
import datetime
token_hello_file = token #Вставьте Ваш токен, полученный от BotFather
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start']) #Для команды /start, можете изменить на любую другую
def start_join(message):
    chat_id=set()
    bot.send_message(message.chat.id, text="Приветствую. Cюда присылаются сообщения из чатов на тему рилсов, когда появляются новые! Если есть дополнительные вопросы - пиши на @ValentinYE")
    user_id = message.from_user.id
    chat_id.add(user_id)

    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute("""CREATE TABLE IF NOT EXISTS id_of_users(
        id  INTEGER PRIMARY KEY AUTOINCREMENT,
        id_users INTEGER,
        date DATE
    )""")
    print('Подключились к базе данных')

    for i in chat_id:
        info = sql.execute(f'SELECT id_users FROM id_of_users WHERE id_users=?', (i,))
        if info.fetchone() is None:
            x = datetime.datetime.now()
            sql.execute(f"""INSERT INTO id_of_users (id ,id_users, date) VALUES (NULL,?,?)""",(i,x))
            db.commit()
            print('Успешно добавили id')
        else:
            pass

    sql.close()
    db.close()
    print(chat_id)
 #Чтобы бот работал бесперебойно, пока запущена программа
bot.polling(none_stop=True)

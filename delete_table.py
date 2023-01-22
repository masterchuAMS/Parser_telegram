import sqlite3

db = sqlite3.connect('server.db')
sql = db.cursor()
sql.execute('DROP TABLE IF EXISTS chat_of_reels')
db.commit()
sql.close()
db.close()

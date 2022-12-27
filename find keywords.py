import csv
import re
import requests
from telegram_bot import token, chat_id
import time
from telethon.tl.types import PeerUser

def key_words():
    with open('chats.csv.', 'r',encoding="UTF-8") as infile, open('keywords.csv', 'w',encoding="UTF-8") as outfile:
        # Create CSV reader and writer objects
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        # Iterate over rows in input file
        keyword_regex = re.compile(r"\b(reels|рилс)\b", re.IGNORECASE)
        all_messages = []
        # Iterate over rows in input file
        for row in reader:
            # Use regular expression to search for keywords in current row
            match = keyword_regex.findall(",".join(row))
            if match:
                # Keywords found - write current row to output file
                writer.writerow(row)
                all_messages.append(row)

    print(all_messages)



    def send_telegram_message(all_messages):
        url = f'https://api.telegram.org/bot{token}/sendMessage'
        for message in all_messages:
            responce = requests.post(url=url, data={'chat_id': chat_id, 'text':message})
        print(responce)
    send_telegram_message(all_messages)


while True:
    key_words()
    time.sleep(86420)

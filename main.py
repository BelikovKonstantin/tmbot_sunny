from pyrogram import Client
import os
import datetime as dt
import time
from dotenv import load_dotenv
import schedule

load_dotenv()

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
CONTACT_ID = 831000111
FIRST_DATE = dt.date(2021, 8, 10)


def job():
    day_later = dt.date.today() - FIRST_DATE
    if day_later.days % 3 == 0:
        with Client('my_account', API_ID, API_HASH) as app:
            app.send_message(CONTACT_ID, 'Сегодня надо дать лекарство Санни')


if __name__ == '__main__':
    schedule.every().day.at("07:00").do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

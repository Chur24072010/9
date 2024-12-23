import sqlite3
conn = sqlite3.connect('weather.db')
conn.execute('''CREATE TABLE IF NOT EXISTS temperature(date TEXT, time TEXT, temperature REAL)''')
import requests

from bs4 import BeautifulSoup

from datetime import datetime
page = requests.get("https://ua.sinoptik.ua/погода-київ")

soup = BeautifulSoup(page.content, 'html.parser')

temperature = soup.find(class_='today-temp').get_text()

now = datetime.now()

date = now.strftime("%Y-%m-%d")

time = now.strftime("%H:%M:%S")
conn.execute("INSERT INTO temperature (date, time, temperature) VALUES (?, ?, ?)", (date, time, temperature))

conn.commit()
conn.close()

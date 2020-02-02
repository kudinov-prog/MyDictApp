import datetime
from manage import translate_yandex
import sqlite3

conn = sqlite3.connect("dict.db") # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()
#cursor.execute("""CREATE TABLE albums
#                  (en text, ru text, date text)
#               """)

class Word():

    def __init__(self, en):
        self.en = en
        self.ru = translate_yandex(en) # вызов функции переводчика и вставка слова
        self.data = datetime.datetime.now()

    def addword(self):
        # добавляет слово в словарь (sql)
        albums = [(self.en, self.ru, self.data)]
        cursor.executemany("INSERT INTO albums VALUES (?, ?, ?)", albums)
        conn.commit()


    def deleteword(self):
        # удаляет слово из словаря
        self.sql = "SELECT * FROM albums WHERE en=?"
        cursor.execute(self.sql, [('hello')])
        print(cursor.fetchall())

new = Word(input("input:"))
new1 = Word(input("input:"))
#new.addword()
#new1.addword()
new.deleteword()
print(new.ru, new1.ru)
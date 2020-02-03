import sqlite3

conn = sqlite3.connect("dict.db") # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()
cursor.execute("""CREATE TABLE albums
                  (en text, ru text, date text)
               """)
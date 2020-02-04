import sqlite3

conn = sqlite3.connect("dict.db") # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()
#cursor.execute("""CREATE TABLE albums
#                  (en text, ru text, date text)
#               """)

cursor.execute("SELECT date FROM albums")  #находит все элементы столбца en в таблице albums

for i in cursor.fetchall():
   print(i)

cursor.execute("SELECT * FROM albums") #находит все элементы таблицы albums
for i in cursor.fetchall():
   print(i)
import datetime
from tkinter import *
from translate import translate_yandex
import sqlite3

conn = sqlite3.connect("dict.db") # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()


class Word():

    def __init__(self, en):
        self.en = en
        self.ru = translate_yandex(en) # вызов функции переводчика и вставка слова
        self.data = datetime.datetime.now()

    def addword(self):
        albums = [(self.en, self.ru, self.data)]
        cursor.executemany("INSERT INTO albums VALUES (?, ?, ?)", albums)
        conn.commit()

    


class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.inst_lbl = Label(self, text = "Введите ниже английское слово для превода:")
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)

        self.in_word = Entry(self)
        self.in_word.grid(row = 1, column = 0, sticky = W)

        self.submit_bttn = Button(self, text = "Перевести", command = self.trans)
        self.submit_bttn.grid(row = 1, column = 1, sticky = W)

        self.text = Text(self, width = 15, height = 1, wrap = WORD)
        self.text.grid(row = 2, column = 0, columnspan = 2, sticky = W)

        self.submit_bttn = Button(self, text = "Добавить слово в словарь", command = self.add_in_dict)
        self.submit_bttn.grid(row = 2, column = 1, sticky = W)

        self.inst_lbl1 = Label(self, text = "Найти слово в моем словаре:")
        self.inst_lbl1.grid(row = 3, column = 0, columnspan = 2, sticky = W)

        self.in_dict = Entry(self)
        self.in_dict.grid(row = 4, column = 0, sticky = W)

        self.submit_bttn = Button(self, text = "Найти!", command = self.find_word)
        self.submit_bttn.grid(row = 4, column = 1, sticky = W)

        self.text_search = Text(self, width = 30, height = 5, wrap = WORD)
        self.text_search.grid(row = 5, column = 0, columnspan = 2, sticky = W)

    def trans(self):
        content = translate_yandex(self.in_word.get())
        self.text.delete(0.0, END)
        self.text.insert(0.0, (content))

    def add_in_dict(self):
        letter = Word(self.in_word.get())
        letter.addword()

    def find_word(self):
        self.sql = "SELECT * FROM albums WHERE en=?"
        cursor.execute(self.sql, [(self.in_dict.get())])
        curs = cursor.fetchall()
        self.text_search.delete(0.0, END)
        self.text_search.insert(0.0, (curs))

root = Tk()
root.title("Main window")
root.geometry("300x300")

app = Application(root)

root.mainloop()

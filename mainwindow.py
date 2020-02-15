import datetime
from tkinter import *
from translate import translate_yandex
import sqlite3

conn = sqlite3.connect("dict.db")
cursor = conn.cursor()

class Word():

    def __init__(self, en):

        """ Создание объекта с параметрами en, ru, data (дата добавления слова)
        """
        self.en = en
        self.ru = translate_yandex(en)
        self.data = datetime.datetime.now()


class Application(Frame):

    def __init__(self, master):

        """ Инициализация приложения
        """

        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):

        """ Функция создает виджеты приложения - кнопки, области ввода и вывода
        """

        # Кнопка создания базы данных
        self.submit_bttn = Button(self, text = "Создать мой словарь!", command = self.create_bd)
        self.submit_bttn.grid(row = 0, column = 0, sticky = W)

        self.inst_lbl = Label(self, text = "Создается единожды при первом запуске!")
        self.inst_lbl.grid(row = 0, column = 1, columnspan = 2, sticky = W)

        # Инициализация области ввода слова
        self.inst_lbl = Label(self, text = "Введите ниже английское слово для превода:")
        self.inst_lbl.grid(row = 1, column = 0, columnspan = 2, sticky = W)

        self.in_word = Entry(self)
        self.in_word.grid(row = 2, column = 0, sticky = W)

        # Кнопка перевода
        self.submit_bttn = Button(self, text = "Перевести", command = self.trans)
        self.submit_bttn.grid(row = 2, column = 1, sticky = W)

        # Область вывода переведенноего слова
        self.text = Text(self, width = 20, height = 3, wrap = WORD)
        self.text.grid(row = 3, column = 0, columnspan = 1, sticky = W)

        # Кнопка добавления слова в словарь
        self.submit_bttn = Button(self, text = "Добавить слово в словарь", command = self.add_in_dict)
        self.submit_bttn.grid(row = 3, column = 1, sticky = W)

        # Подпись
        self.inst_lbl1 = Label(self, text = "Введите слово для поиска в моем словаре:")
        self.inst_lbl1.grid(row = 4, column = 0, columnspan = 2, sticky = W)

        # Область ввода слова для поиска
        self.in_dict = Entry(self)
        self.in_dict.grid(row = 5, column = 0, sticky = W)

        # Кнопка поиска
        self.submit_bttn = Button(self, text = "Найти!", command = self.find_word)
        self.submit_bttn.grid(row = 5, column = 1, sticky = W)

        self.text_search = Text(self, width = 20, height = 2, wrap = WORD)
        self.text_search.grid(row = 6, column = 0, columnspan = 2, sticky = W)

        # Отображение всего словаря
        self.submit_bttn = Button(self, text = "Показать мой словарь", command = self.find_all)
        self.submit_bttn.grid(row = 7, columnspan = 2, sticky = W)

        self.text_search_all = Text(self, width = 30, height = 7, wrap = WORD)
        self.text_search_all.grid(row = 8, column = 0, columnspan = 2, sticky = W)

        
    def trans(self):

        """ Функция обращается к модулю translate.py и вызывает translate_yandex
        """
        content = translate_yandex(self.in_word.get())
        self.text.delete(0.0, END)
        self.text.insert(0.0, (content))

    def add_in_dict(self):

        """ Проверяет наличие слова в базе, если его нет, то добавляет
        """

        self.sql = "SELECT * FROM albums WHERE en=?"
        cursor.execute(self.sql, [(self.in_word.get())])
        curs = cursor.fetchall()

        if len(curs) != 0:
            self.text.delete(0.0, END)
            self.text.insert(0.0, ("Такое слово уже есть в словаре!"))

        else:
            letter = Word(self.in_word.get())
            albums = [(letter.en, letter.ru, letter.data)]
            cursor.executemany("INSERT INTO albums VALUES (?, ?, ?)", albums)
            conn.commit()

    def find_word(self):

        """ Ищет введенное слово в словаре и выводит в область
        """

        self.sql = "SELECT * FROM albums WHERE en=?"
        cursor.execute(self.sql, [(self.in_dict.get())])
        curs = cursor.fetchall()
        self.text_search.delete(0.0, END)
        self.text_search.insert(0.0, (curs))

    def find_all(self):

        """ Выводит весь словарь 
        """

        self.sql_all = cursor.execute("SELECT en, ru FROM albums")
        curs = cursor.fetchall()
        self.text_search_all.delete(0.0, END)
        self.text_search_all.insert(0.0, (curs))

    def create_bd(self):
   
        """ Создает таблицу albums в базе данных dict.db с тремя столбцами en, ru, date
        """

        cursor.execute("""CREATE TABLE albums
                        (en text, ru text, date text)
                        """)


def main():

    """ Создает окно классa Tk, инициализирует класс Application
    """

    root = Tk()
    root.title("Main window")
    root.geometry("410x400")
    app = Application(root)
    root.mainloop()

main()

import datetime
import time
from manage import translate_yandex


class Word():
    #data = datetime.datetime.now()
    def __init__(self, en):
        self.en = en
        self.ru = translate_yandex(en) # вызов функции переводчика и вставка слова
        self.data = datetime.datetime.now()

    def addword():
        pass

    def deleteword():
        pass

new = Word('big')

print(new.ru)
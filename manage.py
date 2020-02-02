import requests
 
def ru_en(t):
    en = [chr(i) for i in range(65, 123)]
    for i in t[:5]:
        if i in en:
            return 'en-ru'
        else:
            return 'ru-en'
 
def translate_yandex(text):
    URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
    KEY = 'trnsl.1.1.20160119T035517Z.50c6906978ef1961.08d0c5ada49017ed764c042723895ffab867be7a'
    TEXT = text
 
    LANG = ru_en(text)
 
    r = requests.post(URL, data={'key': KEY, 'text': TEXT, 'lang': LANG})
    return r.text[r.text.find('['):-1]
 
print(translate_yandex(input(':>')))
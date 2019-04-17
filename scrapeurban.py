#See the last word added to Urban Dictionary
import requests
from bs4 import BeautifulSoup

url = 'http://www.urbandictionary.com/'
page = requests.get(url)
soup =BeautifulSoup(page.text, "lxml")
data = dict()
data['date'] = soup(class_ = 'ribbon')[0].text
data['def'] = soup(class_ = 'meaning')[0].text
data['word'] = soup(class_ = 'word')[0].text
data['example'] = soup(class_ = 'example')[0].text
print (data['date'].strip('u') + data['word'].strip('u'))
print (data['def'].strip('u'))
print (data['example'].strip('u'))


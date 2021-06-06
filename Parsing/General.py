# scraper.py
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.muztorg.ru/product/A023482'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
#f = open('info.txt', 'w',  encoding='utf-8')
#f.write(r.text)
Name = soup.find('meta',property="og:title")
print(Name.text)

# Блок 1: получение артикулов 600 гитар, чтобы по артикулам перебирать страницы с гитарами
Articl = []
# На одной странице 24 гитары, следовательно 25*24 гитар нам хватит для всей таблицы
Number_pages = 1
# В цикле собираем информацию о артикулах гитар
for page in range(Number_pages):
    # Открываем стартовую страницу с гитарами
    url = 'https://www.muztorg.ru/category/akusticheskie-gitary?in-stock=1&pre-order=1&page=%d' % (page)
    r = requests.get(url)

    # Создаем удобную структуру для парсинга
    soup = BeautifulSoup(r.text, 'lxml')

    # Получаем таблицу из артикулов гитар
    Art = soup.find_all('div', class_ = 'id')

    # Добавляем все артикулы в список обрезаю не нужную информацию, оставляя только значения
    for i in Art:
        Articl.append(int(i.text.strip('\n')[10:]))

# Блок 2: Создание на основе 600 гитар 600 строк в DataFrame с нужыми характеристиками
GTA = pd.DataFrame()

for A in Articl:
    url = 'https://www.muztorg.ru/product/A%d' % (A)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    

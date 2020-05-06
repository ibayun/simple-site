import requests
from bs4 import BeautifulSoup

"""while don't touch"""
# resp = requests.get('https://ru.m.wikipedia.org/wiki/Заглавная_страница')
# resp = resp.text
# soup = BeautifulSoup(resp, 'lxml')
# div = soup.find('div', class_='menu toggle-list__list view-border-box')
# links = div.find_all('a', class_='mw-ui-icon mw-ui-icon-before mw-ui-icon-minerva-die')
# link_random = [el.get('href') for el in links]
# print(link_random)


for _ in range(20):
    new_resp = requests.get(
        'https://ru.m.wikipedia.org/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:Random#/random'
    )
    new = new_resp.text
    soup_second = BeautifulSoup(new, 'lxml')
    soup_title = soup_second.find('title').text.split('—')
    tt, s = soup_second.find('div', class_='mw-content-ltr'), soup_second.p.text
    print(soup_title[0])
    print('*'*10)
    print(s)
    print('_'*60)

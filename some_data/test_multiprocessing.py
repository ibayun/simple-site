import csv
from multiprocessing import Pool

import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    soup_title = soup.find('title').text.split('—')[0]
    html_text = soup.p.text
    return soup_title, html_text


def write_csv(data):
    title, text = data
    with open('sw_data_new.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    pass


def all_data(url):
    html = get_html(url)
    data = get_page_data(html)
    print(data[0])
    write_csv(data)


def main():
    url = ['https://ru.m.wikipedia.org/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:Random#/random']*600

    with Pool(10)as p:
        p.map(all_data, url)


if __name__ == '__main__':
    main()

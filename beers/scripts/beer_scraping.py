#!/usr/bin/env python3
"""
Scraping Beers
Url: https://www.ambev.com.br/marcas/cervejas/
"""
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.ambev.com.br/marcas/cervejas/'
url_off = 'file:///media/fcs/Dropbox/Challenges/HBSIS/offline/Cervejas%20-%20Ambev.html'


def request_url(page_url):
    resp = urlopen(page_url)
    return resp


def main():
    resp = request_url(url_off)
    soup = BeautifulSoup(resp, 'html.parser')
    items = soup.find_all('ul', class_='brands-grid__items')
    item = soup.find_all('li', class_='brands-grid__item')
    print(item)
    for i in item:
        print(i)


    beers = [
        {
            'beer_name': '',
            'harmonization': [],
            'type': '',
            'url': '',
            'image_url': '',

        }
    ]


if __name__ == '__main__':
    main()

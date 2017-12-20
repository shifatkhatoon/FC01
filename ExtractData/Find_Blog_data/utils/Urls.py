# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def extracturls():
    Url = 'https://www.thomascook.com/blog/'
    WebPage = requests.get(Url)
    soup = BeautifulSoup(WebPage.text, 'lxml')

    URLS = []

    for Links in soup.find_all(attrs={'class': 'grid-title'}):
        url = Links.find('a').get('href')
        URLS.append(url)
    return URLS
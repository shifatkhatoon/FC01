# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def extracturls():
    URLS = []
    url = "https://www.thomascook.com/blog/wp-admin/admin-ajax.php"
    params = {
        'offset': '20',
        'layout': 'masonry',
        'exclude': 'undefined',
        'from': 'customize',
        'template': 'sidebar',
        'ppp': '645',
        'action': 'penci_more_post_ajax',
        'nonce': '2e93a85f31'
    }
    response = requests.post(url=url, data=params)
    soup = BeautifulSoup(response.text, "lxml")
    for Links in soup.find_all(attrs={'class': 'grid-title'}):
        url = Links.find('a').get('href')
        URLS.append(url)
    print("get all urls")
    return URLS
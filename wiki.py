# -*-coding:utf-8 -*-

import requests
import bs4

response = requests.get('http://zh.wikipedia.org/wiki/AV'+u'女优列表')

soup = bs4.BeautifulSoup(response.text)
names = soup.select('table a')
for name in names:
    print name.get_text()

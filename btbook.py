# -*- coding:utf-8 -*-
import requests
import bs4

def get_info(url):
    try:
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text)
        links = [a.attrs.get('href') for a in soup.select('a.download')]
        for link in links:
            parts = link.split('&')
            print u'标题: ' + parts[1].replace('dn=', '')
            print parts[0]
        return soup
    except:
        return None

def get_url(keyword):
    url = 'http://btbook.net/search/'+keyword
    soup = get_info(url)
    if soup is None:
        return None
    if len(soup.select('div.bottom-pager a')) > 2:
        last_page = soup.select('div.bottom-pager a')[-2].get_text()
        if last_page:
            for index in range(2, int(last_page)):
                next_url = url + '/' + str(index)
                get_info(next_url)
    
def get_name():
    response = requests.get('http://zh.wikipedia.org/wiki/AV'+u'女优列表')

    soup = bs4.BeautifulSoup(response.text)
    names = soup.select('table a')
    for name in names:
        get_url(name.get_text())
if __name__ == '__main__':
    get_name()

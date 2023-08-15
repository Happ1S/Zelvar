from bs4 import BeautifulSoup
import requests
import urllib.request
import os

URL = 'http://zeljevar.wordsland.ru/zelja/library.php'
HOST = 'http://zeljevar.wordsland.ru/zelja/'
HEADERS = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36 OPR/84.0.4316.31 (Edition Yx 08)'
}
 
def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('a', href=True)

    links = []
    for item in items:
        url = item.get('href')
        if url[0]!='#':
            print(url)
            urllib.request.urlretrieve(HOST+url, 'C:/Users/Admin/Desktop/python/console_game/zelvar/sprites/'+os.path.basename(url))


def parser(URL):
    html = get_html(URL)
    if html.status_code == 200:
        cards = get_content(html.text)
        print(cards)
    else:
        print('Error')

parser(URL)
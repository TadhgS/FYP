from requests import get
from urllib.request import urlopen
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

url = "https://www.wattpad.com/467372879-silver-moon-chapter-1"
html = urlopen(url)

bSoup = BeautifulSoup(html, 'lxml')
type(bSoup)
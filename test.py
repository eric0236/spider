import urllib
import requests
from bs4 import BeautifulSoup

url = 'http://www.baidu.com'
data = requests.get(url)
soup = BeautifulSoup(data.text,'lxml')

print (soup)

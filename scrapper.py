from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

try:
	content = urlopen("http://testing-ground.scraping.pro/block")
	soup = BeautifulSoup(content.read(),"lxml")
except HTTPError as he:
	print(he)
	exit()
except AttributeError as ae:
	print(ae)
	exit()

print(soup.h1.text)
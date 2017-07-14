from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

try:
	content = urlopen("http://www.tsetmc.com/Loader.aspx?ParTree=151311&i=27922860956133067")
	soup = BeautifulSoup(content.read(),"lxml")
	print(soup.div)
except HTTPError as he:
	print(he)
	exit()
except AttributeError as ae:
	print(ae)
	exit()


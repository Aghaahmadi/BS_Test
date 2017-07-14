# Web Scraping with Beautiful Soup 4 p.3
# https://www.youtube.com/watch?v=sAuGH1Kto2I&feature=share
import bs4 as bs
import urllib.request

# sauce = urllib.request.urlopen('https://play.google.com/store/apps/details?id=com.anydo&hl=en').read()
sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(sauce,'lxml')

table = soup.find('table')

table_rows = table.find_all('tr')

for tr in table_rows:
	td = tr.find_all('td')
	row = [i.text for i in td]
	print(row)
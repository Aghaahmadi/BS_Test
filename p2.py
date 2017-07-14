# Web Scraping with Beautiful Soup 4 p.2
# https://www.youtube.com/watch?v=kRDrlvO-Oz0&feature=share
import bs4 as bs
import urllib.request

# sauce = urllib.request.urlopen('https://play.google.com/store/apps/details?id=com.anydo&hl=en').read()
sauce = urllib.request.urlopen('http://digiato.com').read()
soup = bs.BeautifulSoup(sauce,'lxml')

# nav = soup.nav
# for url in nav.find_all('a'):
# 	print(url)

# body = soup.body
# for paragraph in body.find_all('p'):
# 	print(paragraph.text)

for h in soup.find_all('h4', class_='blue'):
	print(h.text)
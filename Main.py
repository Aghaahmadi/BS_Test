# https://www.youtube.com/watch?v=aIPqt-OdmS0

import bs4 as bs
import urllib.request

# sauce = urllib.request.urlopen('http://www.asriran.com/fa/news/547597').read()
sauce = urllib.request.urlopen('https://play.google.com/store/apps/details?id=com.anydo&hl=en').read()
soup = bs.BeautifulSoup(sauce,'lxml')

# print(soup.title.string)

for paragraph in soup.find_all('itemprop'):
	s = paragraph.string
	if s == None:
		continue
	print(paragraph.string)
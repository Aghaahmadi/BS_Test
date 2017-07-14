# https://www.youtube.com/watch?v=aIPqt-OdmS0

import bs4 as bs
import urllib.request

# sauce = urllib.request.urlopen('http://www.asriran.com/fa/news/547597').read()
sauce = urllib.request.urlopen('https://play.google.com/store/apps/details?id=com.anydo&hl=en').read()
soup = bs.BeautifulSoup(sauce,'lxml')

# print(soup.get_text())
# for paragraph in soup.find_all('div'):
# 	s = paragraph.text
# 	if s == None:
# 		continue
# 	print(s)

for url in soup.find_all('a'):
	print(url.get('href'))
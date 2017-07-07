import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('http://www.asriran.com/fa/news/547597').read()
soup = bs.BeautifulSoup(sauce,'lxml')

# print(sauce)
print(soup.title.string)
# print(soup.p.string)
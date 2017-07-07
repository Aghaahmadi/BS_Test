from bs4 import BeautifulSoup
soup = BeautifulSoup('http://www.asriran.com/fa/news/547597')

print(soup.prettify())
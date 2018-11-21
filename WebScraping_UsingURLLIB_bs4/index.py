import urllib.request , urllib.error , urllib.parse
from bs4 import BeautifulSoup
url = input("Enter - ")
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_157678.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html , 'html.parser')

tags = soup('span')
L = list()
for tag in tags:
    L.append(float(tag.contents[0]))
print(sum(L))
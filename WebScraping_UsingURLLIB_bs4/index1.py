import urllib.request , urllib.parse , urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
if len(url) < 1: url = 'https://github.com/Ubaid-Manzoor'

position = int(input("Enter Position ")) - 1
iteration = int(input("Enter Iterations ")) + 1
for repeat in range(iteration):
    print(url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    links = list()
    for tag in tags:
        link = tag.get("href", None)
        if str(link).startswith('http'):
            links.append(link)
    if len(links) >= position:
        url = links[position]
    else:
        print("Links out of range")
        quit()



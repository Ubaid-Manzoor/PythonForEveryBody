import xml.etree.ElementTree as ET
import urllib.parse , urllib.error , urllib.request

url = input("Enter url ")
if len(url) < 1: url = "http://py4e-data.dr-chuck.net/comments_157680.xml"
xml = urllib.request.urlopen(url).read()

stuff = ET.fromstring(xml)
counts = stuff.findall('comments/comment/count')
count_lst = []
for count in counts:
    count_lst.append(int(count.text))
print(sum(count_lst))
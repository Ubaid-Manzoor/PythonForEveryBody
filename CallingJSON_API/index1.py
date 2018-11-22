import urllib.request , urllib.parse , urllib.error
import json
import ssl

url = input("Enter Url - ")
if len(url) < 1: url = "http://py4e-data.dr-chuck.net/comments_157681.json"

#Ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


handle = y=urllib.request.urlopen(url , context=ctx)

data = handle.read().decode()

try:
    js = json.loads(data)
except:
    js=None
    quit()

#print(json.dumps(js, indent=4))
counts = list()
for ele in js['comments']:
    counts.append(ele['count'])

print(sum(counts))

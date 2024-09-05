import urllib.request, urllib.parse
import json, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



actualURL = "http://py4e-data.dr-chuck.net/comments_2069358.json"

url = input("Please enter a URL: ")
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_42.json"

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
js = json.loads(data)

count = 0

for person in js["comments"]:
    count += int(person["count"])
    print(count)


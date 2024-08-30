import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

try:
    position = int(input("Please enter position number: "))
    reps = int(input("Please enter the number of repetitions: "))
    failsafe = position + reps 
    url = input("Please enter url: ")
except:
    position = 3
    reps = 4
    url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = 0

while count < reps:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[position-1].get('href', None)
    #print(url)
    count +=1

print(url)

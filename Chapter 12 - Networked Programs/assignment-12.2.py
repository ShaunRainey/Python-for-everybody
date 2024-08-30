import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup

inpt = input("Please select test or actual data: ")

if inpt == "test" or inpt =="test":
   url = "http://py4e-data.dr-chuck.net/comments_42.html"
elif inpt == "actual" or inpt == "Actual":
   url = "http://py4e-data.dr-chuck.net/comments_2069355.html"
else:
   print("Please try again")
   quit()
 
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')

sum = 0
for tag in tags:
   # Look at the parts of a tag
   #print('TAG:',tag)
   #print('URL:',tag.get('href', None))
   #print('Contents:',tag.contents[0])
   #print('Attrs:',tag.attrs)
   sum += int(tag.contents[0])
print(sum)
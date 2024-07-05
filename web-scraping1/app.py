import requests
from bs4 import BeautifulSoup
req=requests.get("https://codeforces.com/")
soup=BeautifulSoup(req.content,"html.parser")
# All html data
print(soup.prettify())
# Title 
print(soup.title.prettify())
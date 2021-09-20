import requests
from bs4 import BeautifulSoup as bs
r = requests.get("https://www.oraesattaitalia.it/")
contenuto = bs(r.text, features="html.parser")
date = contenuto.find("span", {"id": "ctl00_MainContent_Label1"})
print("oggi è", date.text)
from bs4 import BeautifulSoup
import urllib.request as urllib

import re

url = "https://www.kilobet.fr/res.php"

page = urllib.urlopen(url)

soup = BeautifulSoup(page,'html.parser')

miam = soup.find('div',attrs = {'class':'Nom'})
crotte = miam.text
print(int(crotte))

miam2 = soup.find('div',attrs = {'class':'Nombre'})
crotte = miam2.text
print(crotte)



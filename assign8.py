import requests
from bs4 import BeautifulSoup
url="https://whatismyipaddress.com/"
data=requests.get(url,headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
print(data.content)
soup=BeautifulSoup(data.text, 'html.parser')
print(soup.findall(id='ipv4'))

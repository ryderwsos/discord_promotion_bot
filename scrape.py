from urllib import request
from bs4 import BeautifulSoup
import requests

url = "https://cocofreshtea.ca/promotions/"
page = requests.get(url)
promos = []

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.findAll('div', class_ = "et_pb_with_border")
lists.pop()

for item in lists: 
    image = item.find('img')
    src=image.get('src')
    promos.append(src)

print(promos)
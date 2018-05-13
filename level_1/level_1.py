#!/usr/bin/python3


import requests
from bs4 import BeautifulSoup

hodor = {"id": "341", "holdthedoor": "Submit"}
url = 'http://158.69.76.135/level1.php'
for i in range(4096):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    password = soup.find('input', attrs={'name': 'key'})['value']
    headers = {'cookie' : 'HoldTheDoor={}'.format(password)}
    hodor.update({'key': password})
    x = requests.post(url, data=hodor, headers=headers)

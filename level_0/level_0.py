#!/usr/bin/python3


import requests

for i in range(1024):
    hodor = {"id": "341", "holdthedoor": "Submit"}
    page = requests.post('http://158.69.76.135/level0.php', data=hodor)

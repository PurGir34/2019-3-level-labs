# Practice 1

import requests
from bs4 import BeautifulSoup

url = 'https://med.vesti.ru/'

vesti_med_request = requests.get('https://med.vesti.ru/')
vesti_med_content = vesti_med_request.text

parsed_page = BeautifulSoup(vesti_med_content)

print (parsed_page.find_all('h3'))
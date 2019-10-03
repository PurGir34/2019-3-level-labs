import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime, date, time


results =[]
articles=[]
i=str(date(2019,9,19))

big_dic={"url":"https://panorama.pub","creationDate":i,"аrticles":articles}
url = 'https://panorama.pub'
request = requests.get(url)
if request.status_code==200:
	print("Vse normalno")
else: 
	print("Chto-to u nih tam ne tak!")
content = request.text
parsed = BeautifulSoup(content, 'html.parser')
h3_items = parsed.find_all('h3')
for item in h3_items:
    item='"title":'+ item.text
    articles.append(item)
jsonAr = json.dumps({
	"url":"https://panorama.pub",
	"creationDate":i,
	"аrticles":articles
	})
with open("jfile.json", "w") as file:
    file.write(jsonAr)
print(big_dic)
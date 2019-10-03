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
    #print(item.text)
    #item=item.text
    #results.append(item)
    item='"title":'+ item.text
    articles.append(item)
jsonAr = json.dumps({
	"url":"https://panorama.pub",
	"creationDate":i,
	"аrticles":articles
	})
with open("jfile.json", "w") as file:
    file.write(jsonAr)
#with open("jfile.json", "r") as read_file:
#   data = json.load(read_file)
#print(data) НАДО ВЕРНУТЬ 
print(big_dic)
print("hello")
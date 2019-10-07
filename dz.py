import requests
import json
import datetime
import urllib.request
from bs4 import BeautifulSoup

now = datetime.datetime.now()
date = now.strftime("%d-%m-%Y")
url = "https://panorama.pub"
path = "articles.json"
data = {

    "url": url,
    "creationDate": date,
    "articles": ["None"]
}

def get_html(url):
	results = []
	request = requests.get(url)
	content = request.text
	parsed = BeautifulSoup(content, 'html.parser')
	lil = parsed.find_all(class_="np-post-content")
	for pan in lil:
		results.append(pan.text)
	# items=lil.find_all('div',{'class':'widget news_portal_block_posts np-clearfix'})
	# for item in items:
	# lul=item.find('div',{'class' : 'np-post-content'}).find('h3').text
	# print(item)
	# results.append({
	# 'text':lul
	# })
	return (results)


url = 'https://panorama.pub'
print(get_html(url))


def find_articles(lil_html):
    titles = []
    lil_parsed = BeautifulSoup(lil_html,'html.parser')
    lil_article = lil_parsed.find_all(class_='post_new-title')
    for title in lil_article:
        titles.append(title.text.strip())
    return (titles)


def publish_report(path, articles):
    c = []
    for i in articles:
        d = {"title": i}
        c.append(d)
    data["articles"] = c
    with open(path, "w",encoding="utf-8") as write_file:
        json.dump(data, write_file,indent = 2, ensure_ascii=False)
    return (data)


lil_html = get_html(url)
articles = find_articles(lil_html)
publish_report(path,articles)

print(articles)

def structure(file):
    flag = False
    with open(file, "r",encoding="utf-8") as read_file1:
        data_set = json.load(read_file1)
    if data_set["url"] == "https://panorama.pub":
            flag = True
    if len(data_set["articles"]) >= 1:
        flag = True
    for i in data_set["articles"]:
        for key in i:
            if i[key] != None:
                flag=True
                break

    return(flag)

def struc_articles(url):
    flag = False
    lil_html = get_html(url)
    lil_parsed = BeautifulSoup(lil_html, 'html.parser')
    lil_article =  lil_parsed.find_all(class_='post_new-title')
    if  lil_article ==  lil_parsed.find_all(class_='post_new-title'):
         flag= True
    return (flag)

def check_url(url):
    return(urllib.request.urlopen(url).getcode())
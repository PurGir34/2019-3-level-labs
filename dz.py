import requests
import json
import datetime
from bs4 import BeautifulSoup
from flask import Flask
from flask import render_template

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
    request = requests.get(url)
    content = request.text
    if request.status_code != 200:
        print('Chto-to tut ne takb...')
        return 0
    return (content)


def find_articles(lil_html):
    titles = []
    lil_parsed = BeautifulSoup(lil_html,'html.parser')
    lil_article = lil_parsed.find_all('h3')
    for title in lil_article:
        titles.append(title.text.strip())
    return (titles)


def publish_report(path, articles):
    c = []
    for i in articles:
        d = {"title": i}
        c.append(d)
    data["articles"] = c
    with open(path, "w",encoding="utf8") as write_file:
        json.dump(data, write_file,indent = 2, ensure_ascii=False)
    return (data)


def structure(file):
    flag = False
    with open(file, "r",encoding="utf8") as read_file1:
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

#def struc_articles(url):
 #   flag = False
  #  lil_html = get_html(url)
   # lil_parsed = BeautifulSoup(lil_html, 'html.parser')
   # lil_article =  lil_parsed.find_all('h3')
   # if  lil_article ==  lil_parsed.find_all('h3'):
   #      flag= True
   # return (flag)

def check_url(url):
    return(urllib.request.urlopen(url).getcode())
    
    

app = Flask(__name__)

@app.route('/')
def panorama_articles():
    lil_html = get_html(url)
    articles = find_articles(lil_html)
    publish_report(path, articles)
    print(articles)
    
    with open("articles.json", "r", encoding="utf-8") as read_file1:
        data_set = json.load(read_file1)
    return render_template('news.html', url=data_set['url'], date=data_set['creationDate'], articles=articles)

if __name__ == "__main__":
    app.run()

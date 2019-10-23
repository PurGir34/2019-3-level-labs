import requests
import json
import datetime
from bs4 import BeautifulSoup
from flask import Flask, redirect, url_for
from flask import render_template

now = datetime.datetime.now()
date = now.strftime("%d-%m-%Y")
url1 = "https://panorama.pub"
url2 = "https://newsland.com"
url3 = "https://webinnews.ru/"
path1 = "articles1.json"
path2 = "articles2.json"
path3 = "articles3.json"
fas = "date.json"
data = {

    "url": url1,
    "creationDate": date,
    "articles": ["None"]
}
data2 = {

    "url": url2,
    "creationDate": date,
    "articles": ["None"]
}
data3 = {

    "url": url3,
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


def find_articles1(lil_html1):
    titles = []
    lil_parsed = BeautifulSoup(lil_html1, 'html.parser')
    lil_article = lil_parsed.find_all('h3')
    for title in lil_article:
        titles.append(title.text.strip())
    return (titles)
def find_articles2(lil_html2):
    titles = []
    lil_parsed = BeautifulSoup(lil_html2, 'html.parser')
    lil_article = lil_parsed.find_all('a')
    for title in lil_article:
        titles.append(title.text.strip())
    return (titles)
def find_articles3(lil_html3):
    titles = []
    lil_parsed = BeautifulSoup(lil_html3, 'html.parser')
    lil_article = lil_parsed.find_all('h2')
    for title in lil_article:
        titles.append(title.text.strip())
    return (titles)


def publish_report(path, articles):
    c = []
    for i in articles:
        d = {"title": i}
        c.append(d)
    data["articles"] = c
    with open(path, "w", encoding="utf8") as write_file:
        json.dump(data, write_file, indent=2, ensure_ascii=False)
    return (data)
def get_date(date):
    dt=date
    print(dt)
    return(dt)

app = Flask(__name__)


@app.route('/')
def start():

    return render_template('news4.html')


@app.route('/pano')
def panorama_articles():
    lil_html = get_html(url1)
    articles = find_articles(lil_html)
    publish_report(path1, articles)
    # print(articles)

    with open("articles1.json", "r", encoding="utf-8") as read_file1:
        data_set = json.load(read_file1)
    return render_template('news1.html', url=data_set['url'], date=data_set['creationDate'], articles=articles)
@app.route('/newsland')
def newsland_articles():
    lil_html = get_html(url2)
    articles = find_articles(lil_html)
    publish_report(path2, articles)
    # print(articles)

    with open("articles2.json", "r", encoding="utf-8") as read_file1:
        data_set = json.load(read_file1)
    return render_template('news2.html', url=data_set['url'], date=data_set['creationDate'], articles=articles)
@app.route('/webbi')
def webbi_articles():
    lil_html = get_html(url3)
    articles = find_articles(lil_html)
    publish_report(path3, articles)
    # print(articles)

    with open("articles3.json", "r", encoding="utf-8") as read_file1:
        data_set = json.load(read_file1)
    return render_template('news3.html', url=data_set['url'], date=data_set['creationDate'], articles=articles)

@app.route('/yfyg')
def update2():
    now = datetime.datetime.now()
    date = now.strftime("%d-%m-%Y")
   
    return render_template('new.html', date=date)

@app.route('/1ist')
def redir1():
    return redirect(url_for('panorama_articles'))

@app.route('/2ist')
def redir2():
    return redirect(url_for('newsland_articles'))

@app.route('/3ist')
def redir3():
    return redirect(url_for('webbi_articles'))
    

@app.route('/task')
def update2_page():
    return redirect(url_for('update2'))



if __name__ == "__main__":
    app.run()

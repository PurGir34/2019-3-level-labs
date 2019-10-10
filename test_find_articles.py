import unittest
import requests
import json
from dz import find_articles, get_html, publish_report


class MyTestCase(unittest.TestCase):

    def test_number_of_articles(self):
        self.request = get_html("https://panorama.pub")
        self.tittles = find_articles(self.request)
        publish_report("articles.json",  self.tittles)

        with open("articles.json", "r", encoding="utf-8") as read_file:
            data = json.load(read_file)

        self.assertEqual("https://panorama.pub", data['url']) 
        for article in data['articles']:
            self.assertNotEqual("", article['title'])


if __name__ == '__main__': 
    unittest.main()

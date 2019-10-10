import unittest
import requests
from dz import find_articles


class MyTestCase(unittest.TestCase):

    def test_number_of_articles(self):
        url = "https://panorama.pub"
        length_of_dict = len(find_articles(requests.get(url).text)) 
        print(length_of_dict)

if __name__ == '__main__':
    unittest.main()
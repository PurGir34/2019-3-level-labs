import unittest
from dz import find_articles 


class MyTestCase(unittest.TestCase):

    def test_number_of_articles(self):
        url = "https://panorama.pub"
        length_of_dict = len(find_articles(open(url).read())) #gives the total length of the dictionary, this would be equal to the number of items in the dictionary
        self.assertEqual(length_of_dict, 26) #a function to check if two variables are equal

class MyTestCase2(unittest.TestCase):


    def test_of_url(self):
        url = "https://panorama.pub"
        result = check_url(url)
        self.assertEqual(result, 200)

if __name__ == '__main__':
    unittest.main()

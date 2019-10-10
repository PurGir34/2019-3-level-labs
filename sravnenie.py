import unittest
import dz

class MyTestCase(unittest.TestCase):
    def test_allHeaders(self):
        with open("panorama.html", "r", encoding='utf-8') as read_file:

            self.assertEqual(len(dz.find_articles(read_file)), 40)
if __name__ == '__main__':
    unittest.main()
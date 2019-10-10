import unittest
from dz import get_html


class MyTestCase(unittest.TestCase):
    def test_html_page(self):
        url = "https://panorama.pub"
        a = get_html(url)
if __name__ == '__main__':
    unittest.main()

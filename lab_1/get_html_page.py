import unittest
from dz import get_html


class MyTestCase(unittest.TestCase):
    def test_html_page(self):
        url = "https://panorama.pub"
        a = get_html_page(url)
        print(a)
        self.assertEqual(a.status_code, 200)


if __name__ == '__main__':
    unittest.main()
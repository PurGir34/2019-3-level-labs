import unittest
from dz import get_html


class MyTestCase(unittest.TestCase):
    def test_html_page(self):
        request = get_html("https://panorama.pub")
        self.assertNotEqual(request, 0)
if __name__ == '__main__':
    unittest.main()

import unittest
from pages.sign_in_page import SignInPage


class Test(unittest.TestCase):
    sing_in_page = None

    def setUp(self):
        self.sing_in_page = SignInPage()
        self.sing_in_page.navigate_to_sign_in_page()

    def tearDown(self):
        self.sing_in_page.close()

    def test_sign_in(self):
        pass

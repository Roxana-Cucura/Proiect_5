from browser import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import unittest


class BasePage(Browser, unittest.TestCase):

    def wait_for_elem(self, by, selector):
        WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((by, selector)))
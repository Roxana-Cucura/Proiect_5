# facem o clasa ajutataoare pe care o folosim in tot proiectul

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class Browser:
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(10)
    driver.maximize_window()

    def close(self):
        self.driver.close()


'''class Browser:

    def __init__(self):
        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s)
        self.driver.implicitly_wait(10)
        self.driver.set_page_load_timeout(10)
        self.driver.maximize_window()

    def close(self):
        self.driver.close()
'''

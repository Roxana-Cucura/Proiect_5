from pages.sign_in_page import SignInPage
from pages.forgot_password_page import ForgotPasswordPage
from browser import Browser


def before_all(context):
    context.browser = Browser()

    context.forgot_password_page = ForgotPasswordPage()
    context.sign_in_page = SignInPage()


def after_all(context):
    context.browser.close()


'''from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager'''

'''
def before_all(context):
    context.browser = Browser()
    context.sign_in_page = SignInPage()
    context.forgot_password_page = ForgotPasswordPage()



def after_all(context):
    context.browser.close()
'''

# contextul este o cutiuta care contine cate un obiect de tipul fiecarei clase pagina

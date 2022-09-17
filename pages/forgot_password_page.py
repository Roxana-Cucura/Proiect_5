from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    EMAIL_INPUT = (By.XPATH, '//input[@placeholder="Enter your email"]')
    SEND_EMAIL_BTN = (By.XPATH, '//span[text()="Send email"]/parent::button')
    EMAIL_ERROR_MESSAGE = (By.XPATH, '//p[contains(text(),"email")]')
    BACK_TO_LOGIN_LINK = (By.XPATH, '//a[text()="Back to login"]')

    def set_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        sleep(3)

        # asteptam dupa element
        # print('looking for email')
        # self.wait_for_elem(*self.EMAIL_INPUT)
        # print(self.driver.current_url)
        # self.driver.find_element(*self.BACK_TO_LOGIN_LINK).click(
        # self.wait_for_elem(*self.EMAIL_INPUT)

    def click_send_email_btn(self):
        self.driver.find_element(*self.SEND_EMAIL_BTN).click()
        sleep(3)

    def verify_email_error_message(self):
        actual = self.driver.find_element(*self.EMAIL_ERROR_MESSAGE).text
        expected = 'Please enter a valid email address!'
        self.assertEqual(expected, actual, 'Error message is incorrect')
        sleep(3)

        # self.assertEqual(expected, actual, msg='Error message is incorrect')
        # self.assertEqual(expected, actual, "Error is NOT being displayed!!!")

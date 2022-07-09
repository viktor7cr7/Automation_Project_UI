import time
from telnetlib import EC
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators, Registr

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import math

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():

    def __init__(self, browser, url,timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def open(self):
        self.browser.get(self.url)

    def solve_quiz_and_get_code(self):
        prompt = self.browser.switch_to.alert
        x = prompt.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        prompt.send_keys(answer)
        time.sleep(1)
        prompt.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False



    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def should_be_authorized_user(self):
        assert self.is_element_present(*Registr.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def open_korzine(self):
        self.browser.get(self.url)



    def reg_user(self):
        reg_lon = self.browser.find_element(*Registr.pole_login)
        email = str(time.time()) + "@fakemail.org"
        reg_lon.send_keys(email)

        reg_pass = self.browser.find_element(*Registr.pole_password)
        reg_pass.send_keys("BETejEmm321@")

        reg_conf_pass = self.browser.find_element(*Registr.pole_confirm_password)
        reg_conf_pass.send_keys("BETejEmm321@")

        reg_button = self.browser.find_element(*Registr.button_reg)
        reg_button.click()


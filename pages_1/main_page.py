# from .base_page import BasePage
# from selenium.webdriver.common.by import By
# from .locators import MainPageLocators
# from .locators import LoginPageLocators
#
#
#
# class MainPage(BasePage):
#
#     def go_to_login_page(self):
#         login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
#         login_link.click()
#         alert = self.browser.swtitch_to_alert
#         alert.accept()
#
#
#     def should_be_login_link(self):
#         assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"                                                         # self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")
#
#
#     def check_form_login(self):
#         assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Нет формы логина"
#
#     def check_form_registr(self):
#         assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Нет формы регистрации"
#
#     def should_be_login_url(self):
#         login_url = self.browser.current_url
#         assert "login" in login_url,  "Логина нет"


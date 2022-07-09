
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import KorzineLocators, BasePageLocators


class Shop_page(BasePage):
    def add_korzine(self):
        add_koz = self.browser.find_element(*KorzineLocators.korzine)
        add_koz.click()

    def poisk_xx(self):
        add_poisk = self.browser.find_element(*KorzineLocators.poisk_knig_korzine)
        sovp = add_poisk.text
        add_poisk_1 = self.browser.find_element(*KorzineLocators.poisk_do_korz)
        sovp_1 = add_poisk_1.text
        assert sovp == sovp_1

        price_1 = self.browser.find_element(*KorzineLocators.poisc_price)
        price_1_t = price_1.text
        print(price_1_t)

        price_2 = self.browser.find_element(*KorzineLocators.poisc_price_posle)
        price_2_t = price_2.text
        print(price_2_t)
        assert price_1_t == price_2_t


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*KorzineLocators.proverka_nadpisi),'Сообщение об успехе отображается, но не должно'

    def should_not_be_success_message_1(self):
        assert  self.is_disappeared(*KorzineLocators.proverka_nadpisi), "Надпись осталась"

    def proverka_shapki(self):
        poisk_sh = self.browser.find_element(*KorzineLocators.perexod_s_shapki)
        poisk_sh.click()
        korz_push = self.browser.find_element(*KorzineLocators.pustaya_korz)
        korz = korz_push.text
        print(korz)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"











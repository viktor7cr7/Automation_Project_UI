from .base_page import BasePage
from .locators import KorzineLocators, Registr
from .locators import Base_korzine


class BasketPage(BasePage):
    def item_check(self):
        assert self.is_not_element_present(*Base_korzine.item_tovar), "Товар появился, но не должен"


    def korz_check(self):
        click_korz_1 = self.browser.find_element(*Base_korzine.click_korzine)
        click_korz_1.click()

    def chek_pust_lozr(self):
        assert self.browser.find_element(*KorzineLocators.pustaya_korz) , "В корзине есть товары"


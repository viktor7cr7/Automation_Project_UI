import time
import pytest
from .pages_1.login_page import LoginPage
from .pages_1.product_page import Shop_page
from .pages_1.basket_page import BasketPage

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
@pytest.mark.need_review
def test_user_can_add_product_to_basket(browser, link):
    link =f"{link}"
    page = Shop_page(browser,link)
    page.open()
    time.sleep(3)
    page.add_korzine()
    time.sleep(1)
    page.solve_quiz_and_get_code()
    time.sleep(4)
    page.poisk_xx()
    page.open()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = Shop_page(browser,link)
    page.open()
    page.go_to_login_page()
    time.sleep(1)

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/basket/'
    page = BasketPage(browser,link)
    page.open_korzine()
    time.sleep(2)
    page.item_check()
    time.sleep(1)
    page.chek_pust_lozr()


class TestUserAddToBasketFromProductPage():

        @pytest.fixture(scope="function")
        def setup(self,browser):
         login = LoginPage(browser, 'http://selenium1py.pythonanywhere.com/ru/accounts/login/')
         login.open()
         time.sleep(3)
         time.sleep(1)
         login.reg_user()
         time.sleep(5)
         login.should_be_authorized_user()


        def test_user_cant_see_success_message(self,browser,setup):

            link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
            page = Shop_page(browser,link)
            page.open()
            time.sleep(1)
            page.should_not_be_success_message()

        @pytest.mark.need_review
        def test_guest_can_add_product_to_basket(self,browser,setup):
            link ='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
            page = Shop_page(browser,link)
            page.open()
            time.sleep(3)
            page.add_korzine()
            time.sleep(1)
            time.sleep(3)
            page.poisk_xx()
            page.open()

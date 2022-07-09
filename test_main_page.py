import time
import pytest
from .pages_1.product_page import Shop_page
from .pages_1.basket_page import BasketPage

@pytest.mark.login_guest
class TestLoginFromMainPage():
        def test_guest_should_see_login_link(self,browser):
                link = "http://selenium1py.pythonanywhere.com/"
                page = Shop_page(browser, link)
                page.open()
                page.should_be_login_link()
                time.sleep(3)

        def test_guest_can_go_to_login_page(self,browser):
                link = "http://selenium1py.pythonanywhere.com/"
                page = Shop_page(browser,link)
                page.open()
                time.sleep(1)
                page.go_to_login_page()
                time.sleep(2)



        def test_guest_cant_see_product_in_basket_opened_from_main_page(self,browser):
                link = 'http://selenium1py.pythonanywhere.com/'
                page = BasketPage(browser,link)
                page.open_korzine()
                time.sleep(2)
                page.korz_check()
                time.sleep(1)
                page.item_check()





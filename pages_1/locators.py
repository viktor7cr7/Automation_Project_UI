from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class KorzineLocators():
    korzine = (By.CSS_SELECTOR, '[class="btn btn-lg btn-primary btn-add-to-basket"]')
    poisk_knig_korzine = (By.CSS_SELECTOR, '#messages > div strong')
    poisk_do_korz = (By.CSS_SELECTOR, 'div > h1')
    poisc_price = (By.CSS_SELECTOR, '[class="price_color"]')
    poisc_price_posle = (By.XPATH, '//div[@class="alertinner "]/p/strong [1]')
    proverka_nadpisi = (By.XPATH, '//div[@class="alertinner "]/strong [1]')
    perexod_s_shapki = (By.CSS_SELECTOR, 'span > [class="btn btn-default"]')
    pustaya_korz = (By.CSS_SELECTOR, '#content_inner > p')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")

class Base_korzine():
    item_tovar = (By.CSS_SELECTOR, '[class="availability instock"]')
    click_korzine = (By.CSS_SELECTOR, 'span  [class="btn btn-default"]')

class Registr():
    pole_login = (By.CSS_SELECTOR, '#id_registration-email')
    pole_password = (By.CSS_SELECTOR, '#id_registration-password1')
    pole_confirm_password = (By.CSS_SELECTOR, '#id_registration-password2')
    button_reg = (By.CSS_SELECTOR, '[name="registration_submit"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


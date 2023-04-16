from conduit_page import ConduitPage
from configuration import set_chrome_driver_local, set_chrome_driver_remote
import allure

TEST_DATA_POS = {
    'username': 'albert08',
    'email': 'almodo.albertin@almodom.com',
    'password': 'pontY738'
}

TEST_DATA_NEG = {
    'username': 'joe',
    'email': 'almodo.albert'
}


class TestConduit:
    def setup_method(self):
        self.page = ConduitPage(set_chrome_driver_local())
        # self.page = ConduitPage(set_chrome_driver_remote())
        self.page.open()
        self.page.maximize()
        self._data = True
        self.__variable = False

    def teardown_method(self):
        # self.page.quit()
        pass

    @allure.id('TC1')
    @allure.title('Regisztráció - Helyes felhasználói adatokkal')
    def test_registration_pos(self):
        self.page.link_register().click()
        self.page.input_username().send_keys(TEST_DATA_POS['username'])
        self.page.input_email().send_keys(TEST_DATA_POS['email'])
        self.page.input_password().send_keys(TEST_DATA_POS['password'])
        self.page.button_signin_signup().click()
        assert self.page.message_reg_login('Your registration was successful!')

    @allure.id('TC2')
    @allure.title('Regisztráció - Helytelen felhasználói adatokkal')
    def test_registration_neg(self):
        self.page.link_register().click()
        self.page.input_username().send_keys(TEST_DATA_NEG['username'])
        self.page.input_email().send_keys(TEST_DATA_NEG['email'])
        self.page.input_password().send_keys(TEST_DATA_POS['password'])
        self.page.button_signin_signup().click()
        assert self.page.message_reg_login('Email must be a valid email.')

    @allure.id('TC3')
    @allure.title('Bejelentkezés - Helyes felhasználói adatokkal')
    def test_login_pos(self):
        self.page.link_login().click()
        self.page.input_email().send_keys(TEST_DATA_POS['email'])
        self.page.input_password().send_keys(TEST_DATA_POS['password'])
        self.page.button_signin_signup().click()
        assert self.page.link_profile(TEST_DATA_POS['username'])

    @allure.id('TC4')
    @allure.title('Bejelentkezés - Helytelen felhasználói adatokkal')
    def test_login_neg(self):
        self.page.link_login().click()
        self.page.input_email().send_keys(TEST_DATA_NEG['email'])
        self.page.input_password().send_keys(TEST_DATA_POS['password'])
        self.page.button_signin_signup().click()
        assert self.page.message_reg_login('Email must be a valid email.')

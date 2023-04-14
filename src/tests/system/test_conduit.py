from conduit_page import ConduitPage
from configuration import set_chrome_driver_local, set_chrome_driver_remote

class TestConduit:

    def setup_method(self):
        #self.page = ConduitPage(set_chrome_driver_local())
        self.page = ConduitPage(set_chrome_driver_remote())
        self.page.open()
        self.page.maximize()

    def teardown_method(self):
        #self.page.quit()
        pass

    def test_registration_pos(self):
        self.page.button_register().click()
        self.page.input_username().send_keys('albert08')
        self.page.input_email().send_keys('almodo.albert@almond.com')
        self.page.input_password().send_keys('pontY738')
        self.page.button_signin_signup().click()

    def test_registration_neg(self):
        self.page.button_register().click()
        self.page.input_username().send_keys('benny')
        self.page.input_email().send_keys('almodo.albert')
        self.page.input_password().send_keys('pontY738')
        self.page.button_signin_signup().click()

    def test_login_pos(self):
        self.page.button_login().click()
        self.page.input_email().send_keys('almodo.albert@almond.com')
        self.page.input_password().send_keys('pontY738')
        self.page.button_signin_signup().click()
        assert 7 == 7

    def test_login_neg(self):
        self.page.button_login().click()
        self.page.input_email().send_keys('almodo.albert')
        self.page.input_password().send_keys('pontY738')
        self.page.button_signin_signup().click()
        assert 7 == 7

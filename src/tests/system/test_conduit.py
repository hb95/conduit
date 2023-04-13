from conduit_page import ConduitPage
from configuration import set_chrome_driver_local, set_chrome_driver_remote


class TestConduit:
    def setup_method(self):
        self.page = ConduitPage(set_chrome_driver_remote())
        self.page.open()
        self.page.maximize()

    def teardown_method(self):
        self.page.quit()

    def test_login_pos(self):
        self.page.button_login().click()
        assert 7==7

    def test_login_neg(self):
        self.page.button_login().click()
        assert 7==7

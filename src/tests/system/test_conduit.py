from conduit_page import ConduitPage
from configuration import set_chrome_driver


class TestConduit:
    def setup_method(self):
        self.page = ConduitPage(set_chrome_driver())
        self.page.open()

    def teardown_method(self):
        self.page.quit()

    def test_login_pos(self):
        self.page.button_login().click()
        assert 7==7

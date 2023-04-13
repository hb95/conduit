from general_page import GeneralPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Chrome


class ConduitPage(GeneralPage):
    def __init__(self, browser: Chrome):
        super().__init__(browser, 'localhost:1667')

    def button_login(self):
        return WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//a[@class="nav-link"]')))

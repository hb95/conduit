from configuration import set_chrome_driver_local
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = set_chrome_driver_local()

browser.get('http:/localhost:1667')
#browser.maximize_window()

login_button = \
WebDriverWait(browser, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//a[@class="nav-link"]')))[0]
login_button.click()

signin_button = WebDriverWait(browser, 5).until(
    EC.presence_of_element_located((By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')))
signin_button.click()

browser.switch_to.window()
#print(alert.text)

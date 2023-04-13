from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def set_chrome_driver() -> webdriver.Chrome:
    service = Service(executable_path=ChromeDriverManager().install())
    options = Options()
    options.add_experimental_option('detach', True)

    return webdriver.Chrome(service=service, options=options)

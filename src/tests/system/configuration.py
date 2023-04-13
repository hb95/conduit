from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def set_chrome_driver_local() -> webdriver.Chrome:
    service = Service(executable_path=ChromeDriverManager().install())
    options = Options()
    options.add_experimental_option('detach', True)

    return webdriver.Chrome(service=service, options=options)


def set_chrome_driver_remote() -> webdriver.Chrome:
    service = Service(executable_path=ChromeDriverManager().install())
    options = Options()
    options.add_experimental_option('detach', True)
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    return webdriver.Chrome(service=service, options=options)

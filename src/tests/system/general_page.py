from selenium import webdriver


class GeneralPage:
    def __init__(self, browser: webdriver.Chrome, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def quit(self):
        self.browser.quit()

    def refresh(self):
        self.browser.refresh()

    def maximize(self):
        self.browser.maximize_window()

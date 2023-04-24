from general_page import GeneralPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Chrome
from selenium.common.exceptions import TimeoutException


class ConduitPage(GeneralPage):
    def __init__(self, browser: Chrome):
        super().__init__(browser, 'http://localhost:1667/')

    def button_cookies_accept(self):
        try:
            return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(
                (By.XPATH, "//button[@class='cookie__bar__buttons__button cookie__bar__buttons__button--accept']")))
        except:
            return None

    def button_cookies_decline(self):
        try:
            return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(
                (By.XPATH, "//button[@class='cookie__bar__buttons__button cookie__bar__buttons__button--decline']")))
        except:
            return None

    def link_register(self):
        return WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//li[@class="nav-item"]/a[@href="#/register"]')))

    def link_login(self):
        return WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//a[@href="#/login"]')))

    def input_username(self):
        return WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Username"]')))

    def input_email(self):
        return WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Email"]')))

    def input_password(self):
        return WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Password"]')))

    def button_signin_signup(self):
        return WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')))

    def message_reg_login(self, expected_message):
        try:
            return WebDriverWait(self.browser, 5).until(
                EC.text_to_be_present_in_element((By.XPATH, '//div[@class="swal-text"]'), expected_message))
        except TimeoutException:
            return None

    def link_profile(self, username):
        try:
            return WebDriverWait(self.browser, 5).until(
                EC.presence_of_element_located((By.XPATH, f'//a[@href="#/@{username}/"]')))
        except TimeoutException:
            return None

    def link_logout(self):
        try:
            return WebDriverWait(self.browser, 5).until(
                EC.presence_of_element_located((By.XPATH, '//a[@class="nav-link"]/i[@class="ion-android-exit"]')))
        except TimeoutException:
            return None

    def link_yourfeed(self):
        return WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//a[@href="#/my-feed"]')))

    def links_posts(self):
        return WebDriverWait(self.browser, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, '//a[@class="preview-link"]')))

    def links_pages(self):
        return WebDriverWait(self.browser, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, '//ul[@class="pagination"]/li/a')))

    def link_active_page(self):
        return WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//li[@class="page-item active"]/a')))

    def link_new_post(self):
        return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '//a[@href="#/editor"]')))

    def input_given_placeholder(self, phtext):
        return WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, f'//input[@placeholder="{phtext}"]')))

    def textarea_post(self):
        return WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, f'//textarea[@placeholder="Write your article (in markdown)"]')))

    def button_submit_post(self):
        return WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]')))

    def h1(self):
        return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '//h1')))

    def button_post_comment(self):
        return WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//button[@class="btn btn-sm btn-primary"]')))

    def textarea_comment(self):
        return WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//textarea[@placeholder="Write a comment..."]')))

    def p_given_text(self, text):
        try:
            return WebDriverWait(self.browser, 5).until(
                EC.presence_of_element_located((By.XPATH, f'//p[text()="{text}"]')))
        except TimeoutException:
            return None

    def p_comment(self):
        return WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//p[@class="card-text"]')))

    def i_trash_comment(self):
        return WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//i[@class="ion-trash-a"]')))

    def link_settings(self):
        return WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="#/settings"]')))

    def input_username_setting(self):
        return WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Your username"]')))

    def button_update_settings(self):
        return WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')))

    def button_confirm(self):
        return WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//button[@class="swal-button swal-button--confirm"]')))

    def h1_post_titles(self):
        return WebDriverWait(self.browser, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, '//a[@class="preview-link"]/h1')))

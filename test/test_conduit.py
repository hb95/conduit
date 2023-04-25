import time

from data import *
from conduit_page import ConduitPage
from configuration import set_chrome_driver_in_window, set_chrome_driver_headless
import allure
from selenium.webdriver.common.keys import Keys


class TestConduit:
    def setup_method(self):
        #self.page = ConduitPage(set_chrome_driver_in_window())
        self.page = ConduitPage(set_chrome_driver_headless())
        self.page.open()
        self.page.maximize()

    def teardown_method(self):
        self.page.quit()

    # segédfüggvény: regisztráció dictionary-ben megadott tetszőleges adatokkal
    def registration(self, user_data):
        self.page.link_register().click()
        self.page.input_username().send_keys(user_data['username'])
        self.page.input_email().send_keys(user_data['email'])
        self.page.input_password().send_keys(user_data['password'])
        self.page.button_signin_signup().click()

    def login(self, user_data):
        self.page.link_login().click()
        self.page.input_email().send_keys(user_data['email'])
        self.page.input_password().send_keys(user_data['password'])
        self.page.button_signin_signup().click()

    @allure.id('TC1')
    @allure.title('Adatkezelési nyilatkozat elfogadása')
    def test_cookies_accept(self):
        self.page.button_cookies_accept().click()
        time.sleep(1)
        assert self.page.button_cookies_accept() is None

    @allure.id('TC2')
    @allure.title('Adatkezelési nyilatkozat elutasítása')
    def test_cookies_decline(self):
        self.page.button_cookies_decline().click()
        time.sleep(1)
        assert self.page.button_cookies_decline() is None

    @allure.id('TC3')
    @allure.title('Regisztráció - Helyes felhasználói adatokkal')
    def test_registration_pos(self):
        self.registration(TEST_DATA_REG_POS)
        assert self.page.message_reg_login('Your registration was successful!')

    @allure.id('TC4')
    @allure.title('Regisztráció - Helytelen felhasználói adatokkal')
    def test_registration_neg(self):
        self.registration(TEST_DATA_REGANDLOGIN_NEG)
        assert self.page.message_reg_login('Email must be a valid email.')

    @allure.id('TC5')
    @allure.title('Bejelentkezés - Helyes felhasználói adatokkal')
    def test_login_pos(self):
        #self.registration(TEST_DATA_REGANDLOGIN_POS)
        #self.page.refresh()
        self.login(TEST_DATA_REG_POS)
        assert self.page.link_profile(TEST_DATA_REGANDLOGIN_POS['username'])

    @allure.id('TC6')
    @allure.title('Bejelentkezés - Helytelen felhasználói adatokkal')
    def test_login_neg(self):
        self.login(TEST_DATA_REGANDLOGIN_NEG)
        assert self.page.message_reg_login('Email must be a valid email.')

    @allure.id('TC7')
    @allure.title('Kijelentkezés')
    def test_logout(self):
        self.login(TEST_DATA_REGANDLOGIN_POS)
        self.page.link_logout().click()
        assert self.page.link_logout() is None

    @allure.id('TC8')
    @allure.title('Posztok listázása')
    def test_list(self):
        self.login(TEST_DATA_REGANDLOGIN_POS)
        self.page.link_yourfeed().click()
        list_posts = self.page.links_posts()
        assert len(list_posts) > 0

    @allure.id('TC9')
    @allure.title('Több oldalas lista bejárása')
    def test_list_multipage(self):
        self.login(TEST_DATA_REGANDLOGIN_POS)
        list_pages = self.page.links_pages()

        for i, page in enumerate(list_pages):
            page.click()
            assert self.page.link_active_page().text == str(i + 1)

    @allure.id('TC10')
    @allure.title('Új poszt közzététele')
    def test_post_new(self):
        self.login(TEST_DATA_REGANDLOGIN_POS)
        self.page.link_new_post().click()
        title = self.page.input_given_placeholder('Article Title')
        topic = self.page.input_given_placeholder("What's this article about?")
        tags = self.page.input_given_placeholder('Enter tags')
        article = self.page.textarea_post()

        title.send_keys(TEST_DATA_POST['title'])
        topic.send_keys(TEST_DATA_POST['topic'])
        for word in TEST_DATA_POST['tags']:
            tags.send_keys(word)
            tags.send_keys(Keys.ENTER)
        article.send_keys(TEST_DATA_POST['article'])

        self.page.button_submit_post().click()

        assert self.page.h1().text == TEST_DATA_POST['title']

    @allure.id('TC11')
    @allure.title('Kommentelés sorozatos adatbeolvasással')
    def test_comments_from_file(self):
        self.login(TEST_DATA_REGANDLOGIN_POS)
        self.page.links_posts()[0].click()

        with open('test/poem.txt', 'r', encoding='UTF-8') as comment_file:
            comments = comment_file.readlines()

        for line in comments:
            self.page.textarea_comment().send_keys(line)
            self.page.button_post_comment().click()
            assert self.page.p_given_text(line)

    @allure.id('TC12')
    @allure.title('Komment törlése')
    def test_delete_comment(self):
        self.login(TEST_DATA_REGANDLOGIN_POS)
        self.page.links_posts()[0].click()

        # első komment szövegének kinyerése
        comment_text = self.page.p_comment().text
        # első komment törlése
        self.page.i_trash_comment().click()
        # ellenőrzés, hogy tényleg eltűnt-e a komment
        assert self.page.p_given_text(comment_text) is None

    @allure.id('TC13')
    @allure.title('Felhasználónév módosítása')
    def test_edit_username(self):
        self.login(TEST_DATA_REG_POS)
        self.page.link_settings().click()
        username_field = self.page.input_username_setting()
        username_field.clear()
        username_field.send_keys('KossuthLajos')
        self.page.button_update_settings().click()
        self.page.button_confirm().click()
        assert self.page.link_profile('KossuthLajos')

    @allure.id('TC14')
    @allure.title('Adatok exportálása')
    def test_export_titles(self):
        self.login(TEST_DATA_REGANDLOGIN_POS)
        titles = [element.text for element in self.page.h1_post_titles()]

        with open('post_titles.txt', 'w', encoding='UTF-8') as titles_file:
            for title in titles:
                titles_file.write(title + '\n')

        with open('post_titles.txt', 'r', encoding='UTF-8') as titles_file:
            titles_read = titles_file.readlines()

        assert titles_read[0][:-1] == titles[0]

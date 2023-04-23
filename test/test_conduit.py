import time

from conduit_page import ConduitPage
from configuration import set_chrome_driver_local, set_chrome_driver_remote
import allure

TEST_DATA_POS = {
    'username': 'albert08',
    'email': 'almodo.albertinus@almodom.com',
    'password': 'pontY738'
}

TEST_DATA_NEG = {
    'username': 'joe',
    'email': 'almodo.albert'
}


class TestConduit:
    def setup_method(self):
        # self.page = ConduitPage(set_chrome_driver_local())
        self.page = ConduitPage(set_chrome_driver_remote())
        self.page.open()
        # self.page.maximize()
        self._data = True
        self.__variable = False

    def teardown_method(self):
        self.page.quit()
        # pass

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
        self.page.link_register().click()
        self.page.input_username().send_keys(TEST_DATA_POS['username'])
        self.page.input_email().send_keys(TEST_DATA_POS['email'])
        self.page.input_password().send_keys(TEST_DATA_POS['password'])
        self.page.button_signin_signup().click()
        assert self.page.message_reg_login('Your registration was successful!')

    @allure.id('TC4')
    @allure.title('Regisztráció - Helytelen felhasználói adatokkal')
    def test_registration_neg(self):
        self.page.link_register().click()
        self.page.input_username().send_keys(TEST_DATA_NEG['username'])
        self.page.input_email().send_keys(TEST_DATA_NEG['email'])
        self.page.input_password().send_keys(TEST_DATA_POS['password'])
        self.page.button_signin_signup().click()
        assert self.page.message_reg_login('Email must be a valid email.')

    @allure.id('TC5')
    @allure.title('Bejelentkezés - Helyes felhasználói adatokkal')
    def test_login_pos(self):
        self.page.link_login().click()
        self.page.input_email().send_keys(TEST_DATA_POS['email'])
        self.page.input_password().send_keys(TEST_DATA_POS['password'])
        self.page.button_signin_signup().click()
        assert self.page.link_profile(TEST_DATA_POS['username'])

    @allure.id('TC6')
    @allure.title('Bejelentkezés - Helytelen felhasználói adatokkal')
    def test_login_neg(self):
        self.page.link_login().click()
        self.page.input_email().send_keys(TEST_DATA_NEG['email'])
        self.page.input_password().send_keys(TEST_DATA_POS['password'])
        self.page.button_signin_signup().click()
        assert self.page.message_reg_login('Email must be a valid email.')

    @allure.id('TC7')
    @allure.title('Kijelentkezés')
    def test_logout_pos(self):
        self.test_login_pos()
        self.page.link_logout().click()
        assert self.page.link_logout() is None

    @allure.id('TC8')
    @allure.title('Posztok listázása')
    def test_list_pos(self):
        self.test_login_pos()
        self.page.link_yourfeed().click()
        list_post_authors = self.page.links_author()
        assert len(list_post_authors) > 0

    @allure.id('TC9')
    @allure.title('Több oldalas lista bejárása')
    def test_list_multipage_pos(self):
        self.test_login_pos()
        list_pages = self.page.links_pages()

        for i, page in enumerate(list_pages):
            page.click()
            assert self.page.link_active_page().text == str(i + 1)

    @allure.id('TC10')
    @allure.title('Új poszt közzététele')
    def test_post_new(self):
        self.test_login_pos()
        self.page.link_new_post().click()
        title = self.page.input_given_placeholder('Article Title')
        topic = self.page.input_given_placeholder("What's this article about?")
        tags = self.page.input_given_placeholder('Enter tags')
        article = self.page.textarea_post()

        title.send_keys('Csodálatos!')
        topic.send_keys('Hogy készítsünk tökéletes csalamádét?')
        tags.send_keys('savanyúság')
        article.send_keys("""A borkénport és a nátrium benzoátot kevés vízben feloldjuk, majd hozzáöntjük a többi vízhez és az egészet beleöntjük a vödörbe. Hozzáadjuk a cukrot, a sót, az ecetet és a fűszereket, a tormát, a kaprot, a babérlevelet, az egész borsot, a borókabogyót, a mustármagot és a koriandert.
A vödrös (bedobálós) savanyúsághoz zöldségeket - ami bármi lehet: uborka, almapaprika, TV paprika kicsumázva, félbevágva, picike zöld dinnye, karfiol, gyöngyhagyma stb. - alaposan megmossuk, átvizsgáljuk, hogy nem hibásak-e. Beledobáljuk a lébe, majd a tetejét tányérral lezárjuk, hogy a zöldségeket leszorítsuk a lébe, végül lezárjuk a vödör tetejét.
A vödör tartalmát folyamatosan lehet feltölteni, ahogyan teremnek a kertben a zöldségek, vagy ahogyan hozzájutunk egyéb beszerzési forrásból. Kb. 8 nap múlva lesz fogyasztható az eltett savanyúság. """)

        self.page.button_submit_post()
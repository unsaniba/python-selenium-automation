from pages.bestseller_page import BestsellerPage
from pages.blog import Blog
from pages.main_page import MainPage
from pages.header import Header
from pages.not_found_page import NotFoundPage
from pages.search_result_page import SearchResultPage
from pages.signin_page import SignInPage


class Application:

    def __init__(self, driver):
        self.bestseller_page = BestsellerPage(driver)
        self.blog = Blog(driver)
        self.main_page = MainPage(driver)
        self.not_found_page = NotFoundPage(driver)
        self.header = Header(driver)
        self.search_result_page = SearchResultPage(driver)
        self.signin_page = SignInPage(driver)

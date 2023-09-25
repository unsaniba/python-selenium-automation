from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class BestsellerPage(Page):
    BESTSELLER_LINK = (By.CSS_SELECTOR, 'a[href*="nav_cs_bestsellers"]')
    BESTSELLER_5_LINKS = (By.CSS_SELECTOR, 'a[href*="ref=zg_bs_tab"]')
    TOP_LINKS = (By.CSS_SELECTOR, '.zg-item-immersion')

    def open_bestseller(self):
        self.driver.get('https://www.amazon.com/gp/bestsellers/')
        sleep(2)
        self.driver.refresh()
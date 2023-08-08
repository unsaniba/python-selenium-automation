from behave import given, when, then
from selenium.webdriver.common.by import By


BESTSELLER_LINK = (By.ID, 'nav_cs_bestsellers')
FOOTER_LINKS = (By.CSS_SELECTOR, '.1121')


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
    context.driver.find_element(*BESTSELLER_LINK).click()


# @when('Search for a {product}')
# def search_on_amazon(context, product):
#     context.driver.find_element(*SEARCH_FIELD).send_keys(product)

from behave import given, when, then
from selenium.webdriver.common.by import By


SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
ORDERS_BUTTON = (By.ID, 'nav-orders')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterDescItem1111111')


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
    context.driver.maximize_window()


@when('Search for a {product}')
def search_on_amazon(context, product):
    context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    context.driver.find_element(*SEARCH_BUTTON).click()


@when('Click Orders')
def click_on_order(context):
    context.driver.find_element(*ORDERS_BUTTON).click()


@then('Verify footer has {expected_amount} links')
def verify_link_amount(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*FOOTER_LINKS)
    assert len(links) == expected_amount, f'Expected {expected_amount} Links but got {len(links)}'


@then('Verify has many inks are show in the footer')
def verify_many_link(context):
    # context.driver.find_element(*FOOTER_LINKS)
    links = context.driver.find_elements(*FOOTER_LINKS)
    assert len(links) > 1

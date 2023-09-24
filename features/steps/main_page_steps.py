from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from app.application import Application

SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
ORDERS_BUTTON = (By.ID, 'nav-orders')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterDescItem1111111')
SIGNIN_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-signin-button')


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main()


@when('Search for a {product}')
def search_on_amazon(context, product):
    context.app.header.search_product(product)


@when('Click Orders')
def click_on_order(context):
    context.driver.find_element(*ORDERS_BUTTON).click()


@when('Wait for 3 sec')
def wait_sec(context):
    sleep(3)


@then('Verify Sign In is Clickable')
def verify_signin_btn_clickable(context):
    # context.driver.wait.until(
    #     EC.element_to_be_clickable(SIGNIN_BTN),
    #     message='SignIn btn from popup not clickable'
    # )
    context.app.header.verify_signin_btn_clickable()


@then('Verify Sign In disappears')
def verify_signin_btn_disappears(context):
    context.app.header.verify_signin_btn_disappears()


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

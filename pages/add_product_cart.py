from behave import given, when, then
from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://www.amazon.com/BIC-Cristal-Smooth-Ballpoint-10-Count/dp/B000NVPTU2/ref=psdc_1069820_t2_B00004YTPX'
CART_ICON = (By.ID, 'nav-cart')
ADD_TO_CART_BUTTON = (By.ID, 'add-to-cart-button')
EMPTY_CART_MESSAGE = (By.XPATH, "//h1[contains(text(), 'Your Shopping Cart is empty.')]")
CART_SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.a-size-medium-plus.a-color-base.sw-atc-text.a-text-bold')


@given('Open Amazon Product page')
def open_amazon_product_page(context):
    context.driver.get(URL)


@when('Click on cart icon')
def click_on_cart_icon(context):
    context.driver.find_element(*CART_ICON).click()


@then('Verify \'Your Shopping Cart is empty.\' text present')
def verify_empty_cart_text(context):
    context.driver.find_element(*CART_ICON).click()
    expected_text = 'Your Shopping Cart is empty.'
    actual_text = context.driver.find_element(*EMPTY_CART_MESSAGE).text
    assert expected_text == actual_text, f'Error, expected "{expected_text}" not found in actual "{actual_text}"'


@then('Verify the item is added to Cart')
def verify_item_added_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()
    expected_result = 'Added to Cart'
    actual_result = context.driver.find_element(*CART_SUCCESS_MESSAGE).text
    assert expected_result == actual_result, f'Error, expected {expected_result} not found in actual {actual_result}'

# CSS Locators *************************************************************************************************

# Amazon Logo => driver.find_element(By.CSS_SELECTOR, '.a-icon.a-icon-logo'')
# Create account => driver.find_element(By.CSS_SELECTOR, '[class="a-spacing-small"]'))
# Your name => driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')
# Mobile number or email => driver.find_element(By.CSS_SELECTOR, '#ap_email')
# Password => driver.find_element(By.CSS_SELECTOR, '#ap_password')
# Passwords must be at least 6 characters. => driver.find_element(By.CSS_SELECTOR, '[class="a-alert-content"]')
# Re-enter password => driver.find_element(By.CSS_SELECTOR, '#ap_password_check')
# Continue Button=> driver.find_element(By.CSS_SELECTOR, '#continue')
# Conditions of Use => driver.find_element(By.CSS_SELECTOR, 'a[href*="ap_register_notification_condition_of_use"]'))
# Privacy Notice =>  driver.find_element(By.CSS_SELECTOR, 'a[href*="ap_register_notification_privacy_notice"]'))
# Sign in => driver.find_element(By.CSS_SELECTOR, 'a[href*="signin?openid"]')

#***************************************************************************************************

# Behave (BDD) Test Verify Sign ************************************************************

# Feature: Test for Amazon Verify Sign In Page on Amazon
#
#   Scenario: Open Amazon and Click Orders, then Verify Sign In Page
#     Given Open Amazon page
#     When click on "Orders"
#     Then the "Sign In" header is visible

#***********************************************************************************

# Test for BDD Amazon Verify Sign  *********************************************************
from behave import given, when, then
from selenium.webdriver.common.by import By


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
    context.driver.maximize_window()


@when('click on "Orders')
def click_on_order(context):
    context.driver.find_element(By.XPATH, "//*[text()='& Orders']").click()


@then('the "Sign In" header is visible')
def verify_signin(context):
    expected_result = 'Sign in'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, '.a-spacing-small').text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'

#**********************************************************************************

# Behave (BDD) Test Amazon Cart is empty ************************************************************

# Feature: Test for Amazon clicks on the cart icon and verifies that Your Amazon Cart is empty.
#
#   Scenario: Open Amazon and Click Cart, then Verify the Cart is empty.
#     Given Open Amazon page
#     When click on "Cart"
#     Then the "Your Amazon Cart is empty" header is visible

#***********************************************************************************
# Test for BDD Amazon Cart is empty   *********************************************************
from behave import given, when, then
from selenium.webdriver.common.by import By


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
    context.driver.maximize_window()


@when('click on "Cart"')
def click_on_cart(context):
    context.driver.find_element(By.ID, "nav-cart-count").click()


@then('the "Your Amazon Cart is empty" header is visible')
def verify_cart(context):
    expected_result = 'Your Amazon Cart is empty'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, '.a-row.sc-your-amazon-cart-is-empty').text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'

#**********************************************************************************
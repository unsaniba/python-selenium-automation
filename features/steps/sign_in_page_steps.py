from behave import given, when, then
from selenium.webdriver.common.by import By


@then('verify sign in opened')
def verify_signin(context):
    expected_result = 'Sign in'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, '.a-spacing-small').text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'

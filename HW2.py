# """"""""""""""""""""""""""""""""""""""""""""""""""""""""
#
# Amazon logo => driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo' and @aria-label='Amazon']")
#
# Email field => driver.find_element(By.ID, 'ap_email')
#
# Continue button => driver.find_element(By.ID, 'continue')
#
# Conditions of use link => driver.find_element(By.XPATH, "//a[contains(@href, 'ap_signin_notification_condition_of_use')]")
#
# Privacy Notice link => driver.find_element(By.XPATH, "//a[contains(@href, 'ap_signin_notification_privacy_notice')]")
#
# Need help link => driver.find_element(By.XPATH, "//*[@class='a-expander-prompt']")
#
# Forgot your password link => driver.find_element(By.ID, 'auth-fpp-link-bottom')
#
# Other issues with Sign-In link => driver.find_element(By.ID, 'ap-other-signin-issues-link')
#
# Create your Amazon account button => driver.find_element(By.ID, 'createAccountSubmit')
#
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep



# create a new Chrome browser instance
service = Service(executable_path='/Users/uns/QA/python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# populate search field
search = driver.find_element(By.XPATH, "//*[text()='& Orders']").click()


# wait for 4 sec
sleep(4)


# verify  results
expected_result = 'New to Amazon?'
actual_result = driver.find_element(By.XPATH, "//*[@class='a-divider a-divider-break']").text

assert expected_result == actual_result, f"Expected {expected_result} did not match actual {actual_result}"
print('Test Passed')

driver.quit()
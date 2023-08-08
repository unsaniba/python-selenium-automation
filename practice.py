from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep



# create a new Chrome browser instance
service = Service(executable_path='/chromedriver')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.amazon.com/')

search = driver.find_element(By.ID, 'twotabsearchtextbox')

# search = driver.find_element(By.XPATH, "//a[@class='nav-a  ' and @data-csa-c-content-id='nav_cs_bestsellers']")
#
# search = driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon']")
#
# search = driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ']")
#
# search = driver.find_element(By.XPATH, "//*[text()='Best Sellers' and @class='nav-a  ']")

search.clear()
search.send_keys('Car')

# wait for 4 sec
sleep(4)

# click search button
driver.find_element(By.ID, 'nav-search-submit-button').click()

# verify search results
assert 'car' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

DRIVER_PATH = os.environ['ENV_DRIVER_PATH']

driver = webdriver.Chrome(executable_path=DRIVER_PATH)

USER_EMAIL = os.environ['ENV_USER_EMAIL']
USER_PW = os.environ['ENV_USER_PW']
LINKED_URL = 'https://www.linkedin.com/jobs/search/'

driver.get(LINKED_URL)

sign_in_button = driver.find_element_by_xpath('/html/body/nav/div/a[2]')
sign_in_button.click()

user_field = driver.find_element_by_xpath('//*[@id="username"]')
user_field.send_keys(USER_EMAIL)

pw_field = driver.find_element_by_xpath('//*[@id="password"]')
pw_field.send_keys(USER_PW)
pw_field.send_keys(Keys.ENTER)

driver.close()




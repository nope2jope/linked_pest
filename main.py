from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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

job_bar = driver.find_element_by_xpath('//*[@id="jobs-search-box-keyword-id-ember37"]')
job_title = 'developer'
job_bar.send_keys(job_title)

spot_bar = driver.find_element_by_xpath('//*[@id="jobs-search-box-location-id-ember37"]')
job_spot = 'philadelphia'
spot_bar.send_keys(job_spot)

spot_bar.send_keys(Keys.ENTER)

# run code and click back

# from here i need to isolate the ul and accordingly each li
# such that i can iterate through them and fill out predictable fields
# first i should attempt isolating one element -- my mistake might've been
# being too ambitious in attempting the ul from the get

time.sleep(15)

driver.quit()
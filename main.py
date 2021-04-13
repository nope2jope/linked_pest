from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import os

# sleep increments for tests
LONG_WAIT = 10
SHORT_WAIT = 5

# path to chromedriver.exe
DRIVER_PATH = os.environ['ENV_DRIVER_PATH']

# initialize selenium driver w/ chromedriver.exe
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

# user credentials, other constants
# in addition to the user credentials, bot assumes an active/fleshed-out linked in profile
# i.e. an uploaded resume, phone number, etc.
USER_EMAIL = os.environ['ENV_USER_EMAIL']
USER_PW = os.environ['ENV_USER_PW']
LINKED_URL = 'https://www.linkedin.com/jobs/search/'
JOB_TITLE = 'developer'
LOCATION = 'philadelphia'

# driver pulls up job search url, begins process of logging in
driver.get(LINKED_URL)
driver.find_element_by_link_text('Sign in').click()

# sleeping here, or implicit/explicit waiting helps driver find clickable items
# with the added benefit of appearing more human
time.sleep(SHORT_WAIT)

# inputting credentials
user_field = driver.find_element_by_xpath('//*[@id="username"]')
user_field.send_keys(USER_EMAIL)

pw_field = driver.find_element_by_xpath('//*[@id="password"]')
pw_field.send_keys(USER_PW)

# an alternative to click(), sending RETURN where applicable can save testing/finding elements
pw_field.send_keys(Keys.ENTER)

# these elements were harder to access without a longer wait
time.sleep(LONG_WAIT)

# formerly the easy apply filter
easy_button = driver.find_element_by_xpath('//*[@aria-label="Apply on LinkedIn filter."]')
easy_button.click()

time.sleep(LONG_WAIT)

# the nature of these input fields made them easiest to locate and interact with by finding them with find_elements_
bars = driver.find_elements_by_xpath('//*[@role="combobox"]')

# position to search for
job_bar = bars[0]
job_bar.click()
job_bar.send_keys(JOB_TITLE)

# location of interest
spot_bar = bars[1]

# this field is initialized with location data, so should be cleared first
spot_bar.clear()
spot_bar.send_keys(LOCATION)
spot_bar.send_keys(Keys.ENTER)

time.sleep(SHORT_WAIT)

# find_elements_ returns a list of clickable job cards
job_listings = driver.find_elements_by_css_selector('.job-card-container--clickable')

# the loop which does the applying itself
for job in job_listings:
    # some breathing room, visibility on the user's end
    job.click()
    time.sleep(SHORT_WAIT)
    try:
        # each iteration requires a new button variable
        apply_button = driver.find_element_by_class_name('jobs-apply-button')
        apply_button.click()

        submit_button = driver.find_element_by_xpath('//*[@aria-label="Submit application"]')
        submit_button.click()

    # this exception needs to be imported from selenium
    except NoSuchElementException:
        pass

# admire your handiwork
time.sleep(LONG_WAIT)
driver.close()





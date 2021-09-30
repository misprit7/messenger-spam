from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver import FirefoxOptions

import time
import re
from pyvirtualdisplay import Display

import config

# Virtual display, not entirely sure if it works or not but headless works fine
# disp = Display()
# disp.start()

# Makes it run in headless mode for vm usage
opts = FirefoxOptions()
# Comment this out for debugging
# opts.add_argument("--headless")
with webdriver.Firefox(firefox_options=opts) as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("https://messenger.com")
    time.sleep(2)
    print('Navigated to messenger')
    # Private login file as to not put my fb login on github
    driver.find_element(By.ID, "email").send_keys(config.facebook_login['email'])
    driver.find_element(By.ID, "pass").send_keys(config.facebook_login['pw'])
    login_button = driver.find_element(By.ID, 'loginbutton')
    driver.execute_script("arguments[0].click();", login_button)
    time.sleep(3)
    print('Logged in')

    # This doesn't work in headless for some reason, probably since it relies on js to load
    # driver.find_element(By.XPATH, "//a[@href='/t/" + config.target_id + "/']").click()
    driver.get(re.sub('\/t\/[0-9]*\/', '/t/' + config.target_id, driver.current_url))
    time.sleep(3)
    driver.find_elements_by_css_selector("[aria-label=Message]")[0].send_keys('test' + Keys.RETURN)
    print('Sent message')
    time.sleep(20)

# disp.stop()

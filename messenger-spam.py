from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver import FirefoxOptions

import time

import config

#This example requires Selenium WebDriver 3.13 or newer
opts = FirefoxOptions()
# opts.add_argument("--headless")
with webdriver.Firefox(firefox_options=opts) as driver:
    wait = WebDriverWait(driver, 10)
    # driver.get("https://google.com/ncr")
    driver.get("https://messenger.com")
    # WebDriverWait(driver, 10).until(lambda d: d.find_element_by_id('email'))
    time.sleep(2)
    driver.find_element(By.ID, "email").send_keys(config.facebook_login['email'])
    driver.find_element(By.ID, "pass").send_keys(config.facebook_login['pw'])
    driver.find_element(By.ID, 'loginbutton').click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//a[@href='/t/" + config.target_id + "/']").click()
    time.sleep(3)
    driver.find_elements_by_css_selector("[aria-label=Message]")[0].send_keys('test')
    time.sleep(20)
    # driver.find_element(By.NAME, "q").send_keys("cheese" + Keys.RETURN)
    # first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3")))
    # print(first_result.get_attribute("textContent"))
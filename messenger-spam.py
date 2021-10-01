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
import gmail

service = gmail.register()



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

    # get emails that match the query you specify
    results = gmail.search_messages(service, "in:UNREAD")
    # for each email matched, read it (output plain/text to console & save HTML and attachments)
    for msg in results:
        txt = gmail.read_message(service, msg)
        entry = driver.find_elements_by_css_selector("[aria-label=Message]")[0]
        for c in txt:
            if c != '\n':
                entry.send_keys(c)
            else:
                time.sleep(0.1)
                # action = webdriver.ActionChains(driver)
                # action.key_down(Keys.ALT).send_keys_to_element(entry, Keys.RETURN).key_up(Keys.ALT).perform()
                entry.send_keys(Keys.RETURN)
                time.sleep(0.5)
        entry.send_keys(Keys.RETURN)
        print('Sent message')
        time.sleep(5)

    gmail.mark_as_read(service, 'in:UNREAD')


# disp.stop()

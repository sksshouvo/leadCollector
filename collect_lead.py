from selenium.webdriver.common.keys import Keys
from validation.validation import validation
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

class collect_lead:
    def __init__(self):
        self.validation = validation()
        pass

    def collect_lead(self):
        link = input("Your Google Map Link Here:")

        if not self.validation.google_map_check(link):
            return False
        else:
            driver = webdriver.Firefox()
            driver.get(link)
            element = driver.find_element(By.CSS_SELECTOR, "a.hfpxzc")
            href = element.get_attribute('href')
            print("Link", href)
            if href:
                element.send_keys(Keys.CONTROL + Keys.RETURN)
                driver.switch_to.window(driver.window_handles[1])
                print(driver.current_url)
                name_element = driver.find_element(By.TAG_NAME, 'h1')
                print("Name:", name_element.text)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])

            time.sleep(10)
            driver.close()
        pass
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
            element = driver.find_element(By.CLASS_NAME, "hfpxzc")
            
            print(element.get_attribute('href'))
            
            time.sleep(10)
            driver.close()
        pass
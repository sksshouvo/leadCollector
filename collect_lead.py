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
            elements_array = driver.find_elements(By.CLASS_NAME, "hfpxzc")

            for data in elements_array:
                href = data.get_attribute('href')
                # print(href)
                
                # Click on the element to navigate to the link
                if href:
                    data.click()
                    # Perform actions on the newly loaded page
                    new_url = driver.current_url
                    print(f"Current URL after clicking: {new_url}")

                    # Find the element in the new context
                    # xpath_expression = "//h1[@class='DUwDvf lfPIob']"
                    # element = driver.find_element(By.XPATH, xpath_expression)

                    # Print the text value of the found element
                    # print(element.text)
                    # print(f"Current URL after clicking: {new_url}")
                    # Add your actions on the newly loaded page here
                    # Go back to the original page
                    driver.back()
            
            time.sleep(10)
            driver.close()
        pass
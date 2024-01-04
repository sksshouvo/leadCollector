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
                print(href)
                
                # Click on the element to navigate to the link
                if href:
                     # Click on the element to open link in a new tab
                    data.send_keys(Keys.CONTROL + Keys.RETURN)

                    # Switch to the new tab
                    driver.switch_to.window(driver.window_handles[1])
                    print(driver.title)
                    # Now you are on the newly opened tab
                    # Extract information as needed
                    # Example: Find and print the name, phone, and address
                    name_element = driver.find_element(By.CSS_SELECTOR, ".DUwDvf.lfPIob")
                    phone_element = driver.find_element(By.CSS_SELECTOR, ".Io6YTe.fontBodyMedium.kR99db")  # Replace with the actual CSS selector
                    address_element = driver.find_element(By.CSS_SELECTOR, ".Io6YTe.fontBodyMedium.kR99db")  # Replace with the actual CSS selector

                    print("Name:", name_element.text)
                    print("Phone:", phone_element.text)
                    print("Address:", address_element.text)

                    # Close the new tab
                    driver.close()

                    # Switch back to the original tab
                    driver.switch_to.window(driver.window_handles[0])

            time.sleep(10)
            driver.close()
        pass
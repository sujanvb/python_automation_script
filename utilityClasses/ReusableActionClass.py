from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ReusableActionClass:
     
    def __init__(self, driver):
        self.driver = driver

    def waitForVisibility(self, locator):
        try:
            print("Waiting for visibility of element: " + str(locator))
            wait = WebDriverWait(self.driver, 30)
            wait.until(EC.visibility_of_element_located(locator))
        except (Exception) as e:
            print(f"[Exception in waitForVisibility] {e}")

    def waitForClickability(self, locator):
        try:
            print("Waiting for element to be clickable: " + str(locator))
            wait = WebDriverWait(self.driver, 30)
            wait.until(EC.element_to_be_clickable(locator))
        except (Exception) as e:
            print(f"[Exception in waitForClickability] {e}")

    def click(self, locator):
        try:
            print("Clicking element: " + str(locator))
            self.waitForVisibility(locator)
            self.driver.find_element(*locator).click()
        except (Exception) as e:
            print(f"[Exception in clickElement] {e}")

    def isDisplayed(self, locator) -> bool:
        try:
            print("Checking if element is displayed: " + str(locator))
            return self.driver.find_element(*locator).is_displayed()
        except (Exception) as e:
            print(f"[Exception in isDisplayed] {e}")
            return False

    def getText(self, locator) -> str:
        try:
            print("Getting text from element: " + str(locator))
            self.waitForVisibility(locator)
            return self.driver.find_element(*locator).text
        except (Exception) as e:
            print(f"[Exception in getText] {e}")
            return ""

    def clearSetText(self, locator, text: str):
        try:
            print(f"Setting text '{text}' into element: {locator}")
            self.waitForVisibility(locator)              
            element = self.driver.find_element(*locator) 
            element.clear()                              
            element.send_keys(text)
        except (Exception) as e:
            print(f"[Exception in clearSetText] {e}")

    def getAttributeValue(self, locator, attribute_name: str) -> str:
        try:
            print(f"Getting '{attribute_name}' attribute from element: {locator}")
            self.waitForVisibility(locator)                  
            element = self.driver.find_element(*locator)
            return element.get_attribute(attribute_name)
        except (Exception) as e:
            print(f"[Exception in getAttributeValue] {e}")
            return ""

    def getTextOfElements(self, locator) -> list:
        try:
            print("Getting text from all elements: " + str(locator))
            self.waitForVisibility(locator) 
            elements = self.driver.find_elements(*locator)
            return [element.text for element in elements]
        except (Exception) as e:
            print(f"[Exception in getTextOfElements] {e}")
            return []
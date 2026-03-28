
from selenium.webdriver.common.by import By

from pageClasses.MasterPage import MasterPage
from utilityClasses.ReusableActionClass import ReusableActionClass


class HomePage(MasterPage):
    
    shopProductsButton = (By.XPATH, "//a[text()='Shop products']")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = ReusableActionClass(self.driver)
        
    def isPageLoaded(self) -> bool:
        print("Checking if Home Page is loaded")
        self.actions.waitForVisibility(self.shopProductsButton)
        return self.actions.isDisplayed(self.shopProductsButton)
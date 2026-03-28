from selenium.webdriver.common.by import By

from pageClasses.MasterPage import MasterPage
from utilityClasses.ReusableActionClass import ReusableActionClass


class LoginPage(MasterPage):
    
    passwordInputField = (By.XPATH, "//input[@id='password']")
    enterButton = (By.XPATH, "//button[@type='submit']")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = ReusableActionClass(self.driver)
    
    def isPageLoaded(self) -> bool:
        print("Checking if Login Page is loaded")
        self.actions.waitForVisibility(self.passwordInputField)
        return self.actions.isDisplayed(self.passwordInputField)
    
    def enterPassword(self, password: str):
        print(f"Entering password in Password Input Field in Login Page")
        self.actions.clearSetText(self.passwordInputField, password)

    def clickEnterButton(self):
        print(f"Clicking Enter Button in Login Page")
        self.actions.click(self.enterButton)
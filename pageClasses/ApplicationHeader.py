
from selenium.webdriver.common.by import By

from utilityClasses.ReusableActionClass import ReusableActionClass


class ApplicationHeader():

    searchIcon = (By.XPATH, "//details-modal[@class='header__search']//summary//*[local-name()='svg' and contains(@class,'icon-search')]")
    searchInputField = (By.XPATH, "//input[@class='search__input field__input']")
    searchIconInSearchInputField = (By.XPATH, "//button[@class='search__button field__button']")
    
    def __init__(self, driver):
        self.driver = driver
        self.actions = ReusableActionClass(self.driver)
        
    def clickSearchIcon(self):
        print("Clicking on Search Icon in Application Header")
        self.actions.click(self.searchIcon)
        
    def enterTextInSearchInputField(self, text: str):
        print(f"Entering text '{text}' in Search Input Field in Application Header")
        self.actions.clearSetText(self.searchInputField, text)
        
    def clickSearchIconInSearchInputField(self):
        print("Clicking on Search Icon inside Search Input Field in Application Header")
        self.actions.click(self.searchIconInSearchInputField)
        
        
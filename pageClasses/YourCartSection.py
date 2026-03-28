
from selenium.webdriver.common.by import By

from utilityClasses.ReusableActionClass import ReusableActionClass


class YourCartSection:

    yourCartHeader = (By.XPATH, "//h2[text()='Your cart']")
    itemNamesInCart = (By.XPATH, "//table[@class='cart-items']/tbody/tr/td[@class='cart-item__details']/a")
    def quantityOfItemsInCart(self, itemName: str) -> tuple:
        return (By.XPATH, f"//table[@class='cart-items']/tbody/tr[.//td[@class='cart-item__details']/a[text()='{itemName}']]/td[@class='cart-item__quantity']//input")
    
    def __init__(self, driver):
        self.driver = driver
        self.actions = ReusableActionClass(self.driver)
        
    def isYourCartSectionDisplayed(self) -> bool:
        print("Checking if Your Cart section is displayed")
        self.actions.waitForVisibility(self.yourCartHeader)
        return self.actions.isDisplayed(self.yourCartHeader)
    
    def getItemNamesInCart(self) -> list:
        print("Getting the names of items present in Your Cart section")
        itemNames = self.actions.getTextOfElements(self.itemNamesInCart)
        return itemNames
    
    def getQuantityOfItemInCart(self, itemName: str) -> int:
        value = self.actions.getAttributeValue(self.quantityOfItemsInCart(itemName), "value")
        print(f"Quantity of item '{itemName}' in Your Cart section is: " + value)
        return int(value)
    
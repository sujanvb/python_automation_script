
from selenium.webdriver.common.by import By

from pageClasses.MasterPage import MasterPage
from utilityClasses.ReusableActionClass import ReusableActionClass


class ProductPage(MasterPage):

    productName = (By.XPATH, "//div[@class='product__title']/h1")
    addToCartButton = (By.XPATH, "//span[contains(text(),'Add to cart')]/parent::button")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = ReusableActionClass(self.driver)
            
    def isPageLoaded(self) -> bool:
        print("Checking if Product Page is loaded")
        self.actions.waitForVisibility(self.productName)
        return self.actions.isDisplayed(self.productName)
    
    def getProductName(self) -> str:
        value = self.actions.getAttributeValue(self.productName, "innerText")
        print("Product name in Product Page is: " + value)
        return value
    
    def clickAddToCartButton(self):
        print("Clicking on Add to Cart button in Product Page")
        self.actions.click(self.addToCartButton)
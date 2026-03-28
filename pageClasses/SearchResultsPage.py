
from selenium.webdriver.common.by import By

from pageClasses.MasterPage import MasterPage
from utilityClasses.ReusableActionClass import ReusableActionClass


class SearchResultsPage(MasterPage):

    pageLoadedLocator = (By.XPATH, "//h1[text()='Search results']")
    def linkOfInStockProduct(self, instance: int) -> tuple:
        return (By.XPATH, f"(//li[@class='grid__item' and not(.//span[text()='Sold out'])]//h3[@class='card__heading h5']/a)[{instance}]")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = ReusableActionClass(self.driver)
        
    def isPageLoaded(self) -> bool:
        print("Checking if Search Results Page is loaded")
        self.actions.waitForVisibility(self.pageLoadedLocator)
        return self.actions.isDisplayed(self.pageLoadedLocator)
    
    def isOneInstockProductDisplayed(self) -> bool:
        print("Checking if at least one in-stock product is displayed in Search Results")
        self.actions.waitForVisibility(self.linkOfInStockProduct(1))
        return self.actions.isDisplayed(self.linkOfInStockProduct(1))
    
    def getProductNameOfFirstInStockProduct(self) -> str:
        value = self.actions.getAttributeValue(self.linkOfInStockProduct(1), "innerText")
        print("Product name of first in-stock product in Search Results is: " + value)
        return value
    
    def clickOnFirstInStockProduct(self):
        print("Clicking on first in-stock product in Search Results")
        self.actions.click(self.linkOfInStockProduct(1))
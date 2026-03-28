from pageClasses.HomePage import HomePage
from pageClasses.LoginPage import LoginPage
from pageClasses.ApplicationHeader import ApplicationHeader
from pageClasses.SearchResultsPage import SearchResultsPage
from pageClasses.ProductPage import ProductPage
from pageClasses.YourCartSection import YourCartSection
from utilityClasses.DriverScript import DriverScript
from utilityClasses.ReportManager import ReportManager


def run_test():
    driver = DriverScript.get_driver()
    ReportManager.set_driver(driver)

    loginPage = LoginPage(driver)
    homePage = HomePage(driver)
    applicationHeader = ApplicationHeader(driver)
    searchResultsPage = SearchResultsPage(driver)
    productPage = ProductPage(driver)
    yourCartSection = YourCartSection(driver)
    
    url = "https://adnabu-store-assignment1.myshopify.com"
    
    driver.get(url)
    ReportManager.updateTestLog("Navigate to url", "Navigated to url: " + url, "PASS")
    
    if loginPage.isPageLoaded():
        ReportManager.updateTestLog("Verify Login Page is loaded", "Login Page is loaded", "PASS")
    else:
        ReportManager.updateTestLog("Verify Login Page is loaded", "Login Page is not loaded", "FAIL")
        raise Exception("Login Page is not loaded")
    
    loginPage.enterPassword("AdNabuQA")
    loginPage.clickEnterButton()
    
    if homePage.isPageLoaded():
        ReportManager.updateTestLog("Enter password and click Enter<br>Verify Home Page is loaded", "Home Page is loaded", "PASS")
    else:
        ReportManager.updateTestLog("Enter password and click Enter<br>Verify Home Page is loaded", "Home Page is not loaded", "FAIL")
        raise Exception("Home Page is not loaded")
    
    applicationHeader.clickSearchIcon()
    applicationHeader.enterTextInSearchInputField("Snowboards")
    applicationHeader.clickSearchIconInSearchInputField()
    if searchResultsPage.isPageLoaded():
        ReportManager.updateTestLog("Search for 'Snowboards'<br>Verify Search Results Page is loaded", "Search Results Page is loaded", "PASS")
    else:
        ReportManager.updateTestLog("Search for 'Snowboards'<br>Verify Search Results Page is loaded", "Search Results Page is not loaded", "FAIL")
        raise Exception("Search Results Page is not loaded")
    
    if not searchResultsPage.isOneInstockProductDisplayed():
        ReportManager.updateTestLog("Verify at least one in-stock product is displayed in Search Results", "No in-stock product is displayed in Search Results", "FAIL")
        raise Exception("No in-stock product is displayed in Search Results")
    
    productName = searchResultsPage.getProductNameOfFirstInStockProduct().strip()
    
    searchResultsPage.clickOnFirstInStockProduct()
    if productPage.isPageLoaded() and productPage.getProductName() == productName:
        ReportManager.updateTestLog(f"Click on product '{productName}'<br>Verify Product Page is loaded", "Product Page is loaded", "PASS")
    else:
        ReportManager.updateTestLog(f"Click on product '{productName}'<br>Verify Product Page is loaded", "Product Page is not loaded", "FAIL")
        raise Exception("Product Page is not loaded")
    
    productPage.clickAddToCartButton()
    
    if yourCartSection.isYourCartSectionDisplayed():
        ReportManager.updateTestLog(f"Click on Add to Cart button<br>Verify Your Cart section is displayed", "Your Cart section is displayed", "PASS")
    else:
        ReportManager.updateTestLog(f"Click on Add to Cart button<br>Verify Your Cart section is displayed", "Your Cart section is not displayed", "FAIL")
        raise Exception("Your Cart section is not displayed")
    
    cartItems = yourCartSection.getItemNamesInCart()
    quantityOfProductInCart = yourCartSection.getQuantityOfItemInCart(productName)
    
    
    if not cartItems.__len__() == 1:
        ReportManager.updateTestLog("Verify product is added to cart", "The cart has more or less Products than expected", "FAIL")
        raise Exception("The cart has more or less Products than expected")
    elif cartItems[0] != productName:
        ReportManager.updateTestLog("Verify product is added to cart", f"The product in cart is different than expected.<br>Expected: {productName}<br>Actual: {cartItems[0]}", "FAIL")
        raise Exception(f"The product in cart is different than expected.")
    elif not quantityOfProductInCart == 1:
        ReportManager.updateTestLog("Verify product is added to cart", f"The quantity of product in cart is different than expected.<br>Expected: 1<br>Actual: {quantityOfProductInCart}", "FAIL")
        raise Exception(f"The quantity of product in cart is different than expected.")
    else:
        ReportManager.updateTestLog("Verify product is added to cart", "The product is added to cart with correct quantity", "PASS")
        
    DriverScript.quit_driver()
    
if __name__ == "__main__":
    run_test()
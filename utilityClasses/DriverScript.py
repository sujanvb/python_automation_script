from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class DriverScript:

    driver: webdriver.Chrome = None

    @staticmethod
    def get_driver() -> webdriver.Chrome:
        if DriverScript.driver is None:
            service = Service(ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            
            # Disable cache
            options.add_argument("--disable-application-cache")
            options.add_argument("--disk-cache-size=0")

            # Disable cookies/session reuse by using incognito
            options.add_argument("--incognito")

            # Disable extensions and background apps
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-plugins")

            DriverScript.driver = webdriver.Chrome(service=service, options=options)

        return DriverScript.driver

    @staticmethod
    def quit_driver() -> None:
        if DriverScript.driver is not None:
            DriverScript.driver.quit()
            DriverScript.driver = None
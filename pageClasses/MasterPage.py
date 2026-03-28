from abc import ABC, abstractmethod

from utilityClasses.ReusableActionClass import ReusableActionClass


class MasterPage(ABC):
    
    def __init__(self, driver):
        self.driver = driver
        self.actions = ReusableActionClass(self.driver)
        
    @abstractmethod
    def isPageLoaded(self) -> bool:
        pass
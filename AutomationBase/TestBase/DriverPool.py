from selenium import webdriver
from abc import ABC, abstractmethod
from AutomationBase.TestBase.ConfigurationBase import ConfigurationBase

class DriverPool(ABC):
    """
    Class for abstract basis for general driver pool. This class generates and configures drivers
    for the TestBase.

    @type _config: Enum
    @param _conifg: Protected parameter representing general coniguration for all bases

    """
    _config = None

    def __init__(self, config):
        self._conifg = config

    """
    Function that returnes newlly configured driver.

    @returns: new_driver (webdriver)
    """
    def get_driver(self):

        driver = self._get_local_driver()
        new_driver = self._configure_driver(driver)
        new_driver.get((ConfigurationBase.APP_URL.value))

        return new_driver


    """
    Function that returnes newlly configured local driver.

    """
    @abstractmethod
    def _get_local_driver():
        pass
    
    
    """
    Function for driver configuration.

    """
    @abstractmethod
    def _configure_driver(driver):
        pass


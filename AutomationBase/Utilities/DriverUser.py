from abc import ABC, abstractmethod
from selenium import webdriver
from AutomationBase.Utilities.WaitUntil import WaitUntil
import pdb

class DriverUser(ABC):

    _driver = None
    _wait_until = None

    def __init__(self, driver_user):
        self._driver = driver_user._driver
        self._wait_until = driver_user._wait_until


    def __init__(self, driver):
        self._driver = driver
        self._wait_until = WaitUntil(self._driver)


class driverUserWrapper(DriverUser):
    
    _wrapper = None

    def __init__(self, wrap):
        super().__init__(wrap)
        self._wrapper = wrap
from selenium import webdriver
from AutomationBase.TestBase.DriverPool import DriverPool
import pytest
from PIL import ImageGrab
from abc import ABC, abstractmethod
import os
from datetime import datetime

class Test_webDriverTestClassBase(ABC):
    """
    Class for abstract basis for test classes. Creates all the essintial basis for a test class.

    @type _config: Enum
    @param _conifg: Protected parameter representing general coniguration for all bases

    @type _driver_pool: driverPool
    @param _driver_pool: Protected paramter representing a source for generating we browsers

    @type _driver: webdriver
    @param _driver: Protected driver for selenium testing purposes. Used to interact with UI. 
    """
    _config = None
    _driver_pool = None
    _driver = None

    """
    Function for initializing the Testclass. Runs the preinitialize stage, afterwards the initial testing part and at
    the end runs post initialization and general test cleanup.
    
    @returns: None
    """
    def test_initialize(self):
        try:
            self._pre_initizalize()
            self._driver = self._driver_pool.get_driver()
            self._initialize_page()
            self._post_initialize()
            self.t_cleanup('test_init')

        except Exception as ex:
            self.t_cleanup('test_init')
            print(ex)
            raise RuntimeError(ex) from ex

    
    
    """
    Function for cleaning up after finishing running the test. Runs the precleanup stage, the initial cleanup and
    the post cleanup stage.
    
    @returns: None
    """
    def t_cleanup(self, test_name):
        self._pre_cleanup()
        self._cleanup(self._driver, test_name)
        self._post_cleanup()


    
    """
    Function for initializing page. Function that will start all of the tests general assests.

    @returns: None
    """
    @abstractmethod
    def _initialize_page(self):
        pass

    """
    Function for cleanup of the test. Takes a screenshot of the current state, and finishing the current
    driver.

    @type driver: webdriver
    @param driver: driver which should be cleaned up.

    @type driver_name: str
    @param driver_name: the name of the cleaned up driver.

    @returns: None
    """
    def _cleanup(self, driver, test_name, current_path):
        self._save_screenshot(driver, test_name, current_path)
        driver.quit()


    """
    Function for preitialize of the Testclass.
    @returns: None
    """
    @abstractmethod
    def _pre_initizalize(self):
        pass

    """
    Function for postitialize of the Testclass.
    @returns: None
    """
    @abstractmethod
    def _post_initialize(self):
        pass

    """
    Function for precleanup of the Testclass.
    @returns: None
    """
    @abstractmethod
    def _pre_cleanup(self):
        pass

    """
    Function for postcleanup of the Testclass.
    @returns: None
    """
    @abstractmethod
    def _post_cleanup(self):
        pass
    
    
    """
    Function for screenshoting the current state. Designated for the use of the
    _cleanup function.
    @returns: None
    """
    def _save_screenshot(self, driver, test_name, current_path):
        snapshot = ImageGrab.grab()
        save_path = os.path.realpath(current_path) + '\\screenshots'

        if not os.path.exists(save_path):
            os.makedirs(save_path)

        save_path = save_path + f'\\{test_name}_{datetime.now().strftime("%d_%m_%Y_%H:%M:%S")}.png'
        snapshot.save(save_path)
        self._write_screenshot_link(save_path)


    """
    Function for priniting the path of the screenshot to the console.
    @returns: None
    """
    def _write_screenshot_link(self, save_path):
        print('Screenshot created in %s'%(save_path))


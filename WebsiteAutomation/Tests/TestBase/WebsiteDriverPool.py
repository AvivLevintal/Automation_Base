from AutomationBase.TestBase.DriverPool import DriverPool
from WebsiteAutomation.Tests.TestBase.WebsiteConfigurationBase import WebsiteConfiguration
from selenium import webdriver
import logging
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class WebsiteDriverPool(DriverPool):

    def __init__(self, config):
        DriverPool.__init__(self, config)


    def _get_local_driver(self):
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    def _configure_driver(self, driver):
        configured_driver = driver
        configured_driver.maximize_window()
        return configured_driver
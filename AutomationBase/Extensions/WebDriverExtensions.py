
from selenium import webdriver
from selenium.common.exceptions import NoSuchWindowException

class WebDriverExtensions():

    @staticmethod
    def switch_To_tab(driver, index):
        window_handles = driver.window_handles

        if len(window_handles) - 1 < index:
            raise NoSuchWindowException(f'Index {index} excceeds existing windows!')

        driver.switch_to.window(window_handles[index])

    @staticmethod
    def switch_to_last_tab(driver):
        window_handles = driver.window_handles

        if not window_handles:
            raise NoSuchWindowException('No open windows available')
        
        driver.switch_to.window(window_handles[len(window_handles) - 1])

    @staticmethod
    def close_tab(driver):
        driver.close()
        driver.switch_to_last_tab()

    
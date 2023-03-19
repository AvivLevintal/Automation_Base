from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class WebElementExtensions():
    """
    Class for extending the and optimizing the webElement operations.

    """
    @staticmethod
    def clear_and_send_keys(element, text):
        """
        Function that clears the element's input and sends new keys.
                        
        @type element: WebElement
        @param element: target input element.

        @type text: str
        @param text: the text to be sent to the input.

        @returns: None
        """
        element.clear()
        element.send_keys(text)

    @staticmethod
    def get_classes(element):
        """
        Function that returns the classes of the element.
                        
        @type element: WebElement
        @param element: target element.

        @type return: list
        @returns: list of classes.
        """
        return element.get_attribute('class').split(' ')

    @staticmethod
    def is_contains_class_name(element, class_name):
        """
        Function that returns whether an element is part of a class.
                        
        @type element: WebElement
        @param element: target element.

        @type return: Boolean
        @returns: response whether an element is part of a class or not.
        """
        return class_name in element.get_classes()
    
    @staticmethod
    def get_value(element):
        """
        Function that returns the value of the element.
                        
        @type element: WebElement
        @param element: target element.

        @type return: str.
        @returns: the text of the element.
        """
        return element.get_attribute('value')

    @staticmethod
    def get_id(element):
        return element.get_attribute('id')
    
    @staticmethod
    def get_link(element):
        return element.get_attribute('href')

    @staticmethod
    def get_parent(element):
        return element.find_element(By.XPATH, '..')

    @staticmethod
    def get_children(element):
        return element.find_elements(By.XPATH, '*')

    @staticmethod
    def try_find_element(driver, by, out_element):
        out_element = driver.try_find_element(by)
        return out_element != None

    
    @staticmethod
    def try_find_element(driver, by):
        return driver.find_elements(by)[0]

    @staticmethod
    def hover(driver, element):
        ActionChains(driver).move_to_element(element).perform()
        return driver


    
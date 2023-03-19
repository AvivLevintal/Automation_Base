from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class SearchContextExtensions:
    """
    Class for extending the and optimizing the searchContext operations.

    """
    @staticmethod
    def find_element_css(driver, css_selector):
        """
        Function finding a single element based on it's css attributes.
                        
        @type driver: webdriver
        @param driver: webdriver on which the operations should be performed.

        @type css_selector: str
        @param css_selector: the attribute by which we want to find an element.

        @type return: WebElement
        @returns: desired element.
        """
        return driver.find_element(By.CSS_SELECTOR, css_selector)
    
    @staticmethod
    def find_elements_css(driver, css_selector):
        """
        Function finding multiple elements based on their css attributes.
                
        @type driver: webdriver
        @param driver: webdriver on which the operations should be performed.

        @type css_selector: str
        @param css_selector: the attribute by which we want to find the group of elements.

        @type return: WebElement[]
        @returns: desired elements.
        """
        return driver.find_elements(By.CSS_SELECTOR, css_selector)


    @staticmethod
    def find_element_id(driver, id):
        """
        Function finding a single element based on it's id attribute.
                
        @type driver: webdriver
        @param driver: webdriver on which the operations should be performed.

        @type id: str
        @param id: the id attribute assigned to the element we want to find.

        @type return: WebElement
        @returns: desired element.
        """
        return driver.find_element(By.ID, id)
    
    @staticmethod
    def find_elements_id(driver, id):
        """
        Function finding multiple elements based on their id attribute.
                
        @type driver: webdriver
        @param driver: webdriver on which the operations should be performed.

        @type id: str
        @param id: the id attribute assigned to the elements we want to find.

        @type return: WebElement[]
        @returns: desired elements.
        """
        return driver.find_elements(By.ID, id)

    @staticmethod
    def find_first_or_default(driver, by):
        """
        Function that finds and returns the first element found of a certain type, None otherwise.
                        
        @type driver: webdriver
        @param driver: webdriver on which the operations should be performed.

        @type by: By
        @param by: tuple of the format (By, str) for specifying by what, and what to find.

        @type return: WebElement
        @returns: desired element.
        """
        return driver.find_elements(by)[0]

    @staticmethod
    def find_single(self, driver, by):
        """
        Function that finds and returns a single element found. If more than 1 or 0 were found, raises an exception accordingly.
                
        @type driver: webdriver
        @param driver: webdriver on which the operations should be performed.

        @type by: By
        @param by: tuple of the format (By, str) for specifying by what, and what to find.

        @type return: WebElement
        @returns: desired element.
        """
        elements = driver.find_elements(by)
        
        if not elements:
            raise NoSuchElementException(f'No elements were found using {by}')

        self.assert_up_to_one_element_was_found(elements, by)

        return elements[0]



    @staticmethod
    def find_single_or_default(self, driver, by):
        """
        Function that finds and returns a single element found. If more than 1 found, raises an exception accordingly.
                
        @type driver: webdriver
        @param driver: webdriver on which the operations should be performed.

        @type by: By
        @param by: tuple of the format (By, str) for specifying by what, and what to find.

        @type return: WebElement
        @returns: desired element.
        """
        elements = driver.find_by(by)
        self.assert_up_to_one_element_was_found(elements, by)
    
        if elements: return elements[0]
        else: return None

    def assert_up_to_one_element_was_found(elements, by):
        """
        Function that finds and returns a single element found. If more than 1 or 0 were found, raises an exception accordingly.
                
        @type elements: WebElement[]
        @param elements: element list to determine how many element were found

        @type by: By
        @param by: tuple of the format (By, str) for specifying by what, and what to find.

        @returns: None
        """
        if len(elements) > 1:
            raise ValueError(f'More than one element was found using {by}')
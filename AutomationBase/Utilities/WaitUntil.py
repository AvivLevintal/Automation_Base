from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from multipledispatch import dispatch
import pdb

class WaitUntil():

    _driver = None
    default_timeout = 20
    polling_interval = 0.2

    def __init__(self, driver):
        self._driver = driver


    @staticmethod
    def element_exists_extended(self, search_context, by, timeout=default_timeout):
        sw = time.perf_counter()
        is_first_search = True
        returned_element = None
        while True:

            if not is_first_search:
                time.sleep(self.polling_interval)

            returned_element = search_context.find_elements(by)

            if is_first_search:
                is_first_search = False

            if returned_element != None or sw - time.perf_counter() >= timeout:
                break

        if returned_element == None:
            raise TimeoutException(f"Element was not found by {by} after {timeout} seconds")
        
        return returned_element    
    
    def element_exists(self, by, timeout=default_timeout):
        return WebDriverWait(self._driver, timeout).until(EC.presence_of_element_located(by))

    @staticmethod
    def elements_exists_extended(self, search_context, by, timeout=default_timeout):

        sw = time.perf_counter()
        is_first_search = True
        returned_elements = None
        while True:

            if not is_first_search:
                time.sleep(self.polling_interval)

            returned_elements = search_context.find_elements(by)

            if is_first_search:
                is_first_search = False

            if len(returned_elements) != 0 or sw - time.perf_counter() >= timeout:
                break

        if len(returned_elements) == 0:
            raise TimeoutException(f"Elements were not found by {by} after {timeout} seconds")
        
        return returned_elements


    def element_does_not_exist(self, by, timeout=default_timeout):
        return WebDriverWait(self._driver, timeout).until(lambda dr: dr.find_elements(by).size == 0)

    @staticmethod
    def element_does_not_exist_extended(self, search_context, by, timeout=default_timeout):
        sw = time.perf_counter()
        is_first_search = True
        found_elements = None
        while True:

            if not is_first_search:
                time.sleep(self.polling_interval)

            found_elements = search_context.find_elements(by)

            if is_first_search:
                is_first_search = False

            if len(found_elements) <= 0 or sw - time.perf_counter() >= timeout:
                break

        if len(found_elements) > 0:
            raise TimeoutException(f"Element was not found by {by} after {timeout} seconds")
        
        return True

    def element_is_visible(self, by, timeout=default_timeout):
        return WebDriverWait(self._driver, timeout).until(EC.visibility_of_element_located(by))
    
    @staticmethod
    def element_is_still_visible(self, element, timeout=default_timeout):
        return self._element_satisfies_condition(element, f"Element {element} is still displayed", lambda el: not el.is_displayed(), timeout)

    @staticmethod
    def element_is_disabled(self, element, timeout=default_timeout):
        return self._element_satisfies_condition(element, f"Element {element} is still enabled", lambda el: not el.is_enabled(), timeout)

    def url_satisfies_condition(self, url_predicate, timeout=default_timeout):
        return WebDriverWait(self._driver, timeout).until(lambda driver: driver.current_url if (url_predicate(driver.current_url)) else None)

    def url_is_not_empty(self, timeout=default_timeout):
        return self.url_satisfies_condition(lambda url: not url)
    
    def url_starts_with(self, expected_partial_url, timeout=default_timeout):
        return self.url_satisfies_condition(lambda url: url.startswith(expected_partial_url))

    @staticmethod
    def element_is_stale(self, element, timeout=default_timeout):
        self._element_satisfies_condition(element, "Element didn't become stale", lambda el: __attribute_exists(el))
        def __attribute_exists(el):
            try:
                el.get_attribute('id')
                return False
            except StaleElementReferenceException as ex:
                return True
    
    @staticmethod
    def element_has_class(self, element, class_name, timeout=default_timeout):
        return self._element_satisfies_condition(element, "Element stiil does not have a class " + class_name, 
                                                lambda el: class_name in el.get_attribute('class').split(' '), timeout)
    
    @staticmethod
    def element_class_not_assigned(self, element, class_name, timeout=default_timeout):
        return self._element_satisfies_condition(element, "Element still has the given class" + class_name,
                                                lambda el: el.value_of_css_property("overflow") == "visible", timeout)

    def element_start_moving(self, element, timeout=default_timeout, polling_interval=polling_interval):
        initial_location = None
        second_location = None
        sw = time.perf_counter()

        while True:
            initial_location = element.location
            time.sleep(polling_interval)
            second_location = element.location

            if initial_location != second_location or sw - time.perf_counter() >= timeout:
                break

        if initial_location == second_location:
            raise TimeoutException(f"Element is still for {timeout} seconds. Position is: {second_location}")

        return element
    
    @staticmethod
    def element_stop_moving(self, element, timeout=default_timeout, polling_interval=polling_interval):
        initial_location = None
        second_location = None
        sw = time.perf_counter()

        while True:
            initial_location = element.location
            time.sleep(polling_interval)
            second_location = element.location

            if initial_location == second_location or sw - time.perf_counter() >= timeout:
                break

        if initial_location != second_location:
            raise TimeoutException(f"Element is still moving after {timeout} seconds. Position is: {second_location}")

        return element
    
    @staticmethod 
    def element_stop_resizing(self, element, timeout=default_timeout, polling_interval=polling_interval):
        initial_location = None
        second_location = None
        sw = time.perf_counter()

        while True:
            initial_location = element.size
            time.sleep(polling_interval)
            second_location = element.size

            if initial_location == second_location or sw - time.perf_counter() >= timeout:
                break

        if initial_location != second_location:
            raise TimeoutException(f"Element is still resizing for {timeout} seconds. Latest size is: {second_location}")

        return element


    @staticmethod
    def element_has_size(self, element, timeout=default_timeout):
        return self._element_satisfies_condition(element, lambda el: el.size.height * el.size.width != 0, timeout)

    @staticmethod
    def _element_satisfies_condition(self, element, predicate, timeout=default_timeout):
        return self._element_satisfies_condition(element, "Element didn't satisfy a predicate", predicate, timeout)

    @staticmethod
    def _element_satisfies_condition(self, element, failure_message, predicate, timeout=default_timeout):
        sw = time.perf_counter()
        while time.pref_counter() - sw < timeout:

            if predicate(element):
                return element

            time.sleep(self.polling_interval)
        
        raise TimeoutException(f"{failure_message} after timout of {timeout} seconds") 
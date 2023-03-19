from WebsiteAutomation.Infrastructure.Componants.ComponantBase import ComponantBase
from AutomationBase.Extensions.SearchContextExtensions import SearchContextExtensions
from selenium.webdriver.common.by import By

class InputBase(ComponantBase):
    

    def __init__(self, driver, input_id, parent_element):
        ComponantBase.__init__(self, driver=driver, parent_element=parent_element)
        self._wait_until.element_exists(by=(By.ID, input_id))
        self.componant = SearchContextExtensions.find_element_id(self._driver ,input_id)
        

    def send_keys(self, to_send):
        self.componant.send_keys(to_send)
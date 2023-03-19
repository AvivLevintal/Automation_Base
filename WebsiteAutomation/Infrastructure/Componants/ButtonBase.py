from WebsiteAutomation.Infrastructure.Componants.ComponantBase import ComponantBase
from AutomationBase.Extensions.SearchContextExtensions import SearchContextExtensions
from selenium.webdriver.common.by import By

class ButtonBase(ComponantBase):
    

    def __init__(self, driver, button_id, parent_element):
        ComponantBase.__init__(self, driver=driver, parent_element=parent_element)
        self._wait_until.element_exists(by=(By.ID, button_id))
        self.componant = SearchContextExtensions.find_element_id(self._driver ,button_id)
        

    def click(self):
        self.componant.click()
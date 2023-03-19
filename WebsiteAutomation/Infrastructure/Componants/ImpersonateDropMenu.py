from WebsiteAutomation.Infrastructure.Componants.ButtonBase import ButtonBase
from WebsiteAutomation.Tests.TestBase.WebsiteConfigurationBase import WebsiteConfiguration
from WebsiteAutomation.Infrastructure.Componants.ComponantBase import ComponantBase
from AutomationBase.Extensions.SearchContextExtensions import SearchContextExtensions
from selenium.webdriver.common.by import By

class ImpersonateDropMenu(ButtonBase):
    
    target = None
    selected_target = None

    def __init__(self, driver, parent_element, target):
        ButtonBase.__init__(self, driver, WebsiteConfiguration.IMPERSONATE_MENU.value, parent_element)
        self.target = target

    def select_target(self):
        self.componant.click()
        self._wait_until.element_exists(by=(By.ID, self.target))
        self.selected_target = SearchContextExtensions.find_element_id(self._driver ,self.target)
        self.selected_target.click()
        
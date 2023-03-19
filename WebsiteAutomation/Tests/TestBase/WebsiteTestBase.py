from AutomationBase.TestBase.WebDriverTestClassBase import Test_webDriverTestClassBase
from WebsiteAutomation.Tests.TestBase.WebsiteConfigurationBase import WebsiteConfiguration
from WebsiteAutomation.Tests.TestBase.WebsiteDriverPool import WebsiteDriverPool
from WebsiteAutomation.Infrastructure.Pages.LoginPage import LoginPage
from WebsiteAutomation.Infrastructure.Pages.MainPage import MainPage
import pdb
import os

class WebsiteTestBase(Test_webDriverTestClassBase):
    
    login_page = None
    main_page = None

    def _pre_initizalize(self):
        self._config = WebsiteConfiguration
        self._driver_pool = WebsiteDriverPool(self._config)
        self._driver = self._driver_pool.get_driver()
        
    def _initialize_page(self):
        self.login_page = LoginPage(self._driver)
        self.main_page = MainPage(self._driver)


    def _cleanup(self, driver, driver_name):
        return super()._cleanup(driver, driver_name, os.path.dirname(__file__))


    def _post_initialize(self):
        pass

    def _pre_cleanup(self):
        pass

    def _post_cleanup(self):
        pass
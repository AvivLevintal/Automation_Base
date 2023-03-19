from WebsiteAutomation.Infrastructure.Pages.BasePage import BasePage
from AutomationBase.Extensions.SearchContextExtensions import SearchContextExtensions
from selenium.webdriver.common.by import By
import pdb
import time
from WebsiteAutomation.Tests.TestBase.WebsiteConfigurationBase import WebsiteConfiguration
from WebsiteAutomation.Infrastructure.Componants.SidenavImpersonate import SidenavImpersonate
from WebsiteAutomation.Infrastructure.Componants.ImpersonateFeatureButton import ImpersonateFeatureButton
from WebsiteAutomation.Infrastructure.Componants.ImpersonateDropMenu import ImpersonateDropMenu
from WebsiteAutomation.Infrastructure.Componants.StartImpersonateButton import StartImpersonateButton


class MainPage(BasePage, SearchContextExtensions):

    
    sidenav_impersonate = None
    impersonate_feature_button = None
    impersonate_drop_menu = None
    start_impersonation_button = None


    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def start_impersonation(self, target):
        self.sidenav_impersonate = SidenavImpersonate(self._driver, None)
        self.sidenav_impersonate.click()

        self.impersonate_feature_button = ImpersonateFeatureButton(self._driver, None)
        self.impersonate_feature_button.click()

        self.impersonate_drop_menu = ImpersonateDropMenu(self._driver, None, WebsiteConfiguration.USERNAME_USER.value)
        self.impersonate_drop_menu.select_target()

        self.start_impersonation_button = StartImpersonateButton(self._driver, None)
        self.start_impersonation_button.click()

        time.sleep(5)
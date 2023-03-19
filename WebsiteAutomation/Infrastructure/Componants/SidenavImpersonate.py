from WebsiteAutomation.Infrastructure.Componants.ButtonBase import ButtonBase
from WebsiteAutomation.Tests.TestBase.WebsiteConfigurationBase import WebsiteConfiguration

class SidenavImpersonate(ButtonBase):
    

    def __init__(self, driver, parent_element):
        ButtonBase.__init__(self, driver, WebsiteConfiguration.IMPERSONATE_SIDEBAR.value, parent_element)
        
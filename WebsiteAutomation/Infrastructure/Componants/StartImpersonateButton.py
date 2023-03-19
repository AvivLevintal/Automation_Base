from WebsiteAutomation.Infrastructure.Componants.ButtonBase import ButtonBase
from WebsiteAutomation.Tests.TestBase.WebsiteConfigurationBase import WebsiteConfiguration

class StartImpersonateButton(ButtonBase):
    

    def __init__(self, driver, parent_element):
        ButtonBase.__init__(self, driver, WebsiteConfiguration.START_IMPERSONATE_BUTTON.value, parent_element)
        
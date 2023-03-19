from WebsiteAutomation.Infrastructure.Componants.InputBase import InputBase
from WebsiteAutomation.Tests.TestBase.WebsiteConfigurationBase import WebsiteConfiguration

class PasswordInput(InputBase):
    
    def __init__(self, driver, parent_element):
        InputBase.__init__(self, driver, WebsiteConfiguration.PASSWORD_INPUT.value, parent_element)
        
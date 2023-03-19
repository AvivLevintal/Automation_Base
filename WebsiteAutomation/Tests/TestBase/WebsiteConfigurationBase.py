from AutomationBase.TestBase.ConfigurationBase import ConfigurationBase
from enum import Enum


class WebsiteConfiguration(Enum):
    #General config
    APP_URL = 'http://localhost:4200'
    LOCAL_DRIVER_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\Chrome Driver\\chromedriver.exe'

    #Credentials
    USERNAME_INTERNAL = 'TEST_USERNAME_ADMIN'
    PASSWORD_INTERNAL = 'TEST_PASSWORD'
    USERNAME_USER = 'TEST_USERNAME'

    #Componants - Temporary
    USERNAME_INPUT = 'username_input'
    PASSWORD_INPUT = 'password_input'
    LOGIN_BUTTON = 'login_button'
    IMPERSONATE_SIDEBAR = 'sidenav_internal_dash'
    IMPERSONATE_FEATURE_BUTTON = 'impersonate_feature_button'
    IMPERSONATE_MENU = 'impersonate_menu'
    START_IMPERSONATE_BUTTON = 'start_impersonate_button'
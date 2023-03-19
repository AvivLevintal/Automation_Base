from WebsiteAutomation.Infrastructure.Pages.BasePage import BasePage
from AutomationBase.Extensions.SearchContextExtensions import SearchContextExtensions
from selenium.webdriver.common.by import By
import pdb
import time
from WebsiteAutomation.Infrastructure.Componants.LoginButton import LoginButton
from WebsiteAutomation.Infrastructure.Componants.PasswordInput import PasswordInput
from WebsiteAutomation.Infrastructure.Componants.UsernameInput import UsernameInput

class LoginPage(BasePage, SearchContextExtensions):

    login_button = None
    username_input = None
    password_input = None

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.login_button = LoginButton(driver, None)
        self.username_input = UsernameInput(driver, None)
        self.password_input = PasswordInput(driver, None)
    
    def login(self, username, password):
        
        self.username_input.send_keys(username)
        self.password_input.send_keys(password)
        self.login_button.click()    

    def start_impersonation(self, target):
        pass
import pytest
from WebsiteAutomation.Tests.TestBase.WebsiteTestBase import WebsiteTestBase
import pdb


class Test_website(WebsiteTestBase):

    def test_login(self):
        self._pre_initizalize()
        self._initialize_page()
        self.login_page.login(self._config.USERNAME_INTERNAL.value, self._config.PASSWORD_INTERNAL.value)
        self.t_cleanup('test_login')


    def test_impersonate(self):
        self._pre_initizalize()
        self._initialize_page()
        self.login_page.login(self._config.USERNAME_INTERNAL.value, self._config.PASSWORD_INTERNAL.value)
        self.main_page.start_impersonation(self._config.USERNAME_USER.value)
        self.t_cleanup('test_impersonate')


    def __str__(self):
        return f"{self.main_page}, {self._driver}, {self._driver_pool}"
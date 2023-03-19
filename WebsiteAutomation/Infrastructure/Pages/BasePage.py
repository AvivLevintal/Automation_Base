from abc import ABC
from AutomationBase.Utilities.DriverUser import DriverUser
import pdb


class BasePage(DriverUser, ABC):

    def __init__(self, driver):
        DriverUser.__init__(self, driver)

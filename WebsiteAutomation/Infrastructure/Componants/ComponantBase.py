from abc import ABC
from AutomationBase.Utilities.DriverUser import DriverUser


class ComponantBase(DriverUser, ABC):

    _parent_element = None
    componant = None

    def __init__(self, driver, parent_element):
        DriverUser.__init__(self, driver=driver)
        self._parent_element = parent_element

from enum import Enum

class ConfigurationBase(Enum):
    """
    Enum that represents general conifuration

    @param APP_URL: url of the tested site
    @param LOCAL_DRIVER_PATH: the path of the used driver on the current computer
    """
    APP_URL = 'http://localhost:4200'
    LOCAL_DRIVER_PATH = 'C:\Program Files\Google\Chrome\Application\Chrome Driver\chromedriver.exe'
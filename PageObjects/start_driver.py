from PageObjects.driver import Driver
from PageObjects.login_page import LoginPage


class StartDriver(object):

    @classmethod
    def goto_loginPage(cls):
        Driver.start_driver()
        return LoginPage()




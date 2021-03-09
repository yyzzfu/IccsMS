import pytest
from PageObjects.home_page import HomePage
from PageObjects.start_driver import StartDriver

homepage: HomePage = None


@pytest.fixture(scope='session')   # 所有的.py文件只运行一次
def enter_the_homepage():
    global homepage    # 声明全局变量
    homepage = StartDriver.goto_loginPage().login()
    yield homepage
    homepage.driver.quit()


@pytest.fixture()   # 每个测试用例都执行一次
def refresh():
    global homepage   # 全局变量
    homepage.refresh_page()


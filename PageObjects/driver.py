from selenium import webdriver


class Driver:

    driver: webdriver

    @classmethod
    def start_driver(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        url = 'http://172.17.46.198:9080/IccsMS'
        cls.driver.get(url)
        return cls.driver


# a = StartDriver.start_driver()
#
# print(StartDriver.driver)

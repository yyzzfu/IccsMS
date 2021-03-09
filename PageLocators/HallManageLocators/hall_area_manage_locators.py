from selenium.webdriver.common.by import By


class HallAreaManageLocators:

    # 区域名称
    hall_area_name = (By.XPATH, ".//*[@id='name']")
    # 修改按钮
    modify_button = (By.XPATH, "//*[@id='contentTable']//a[contains(text(), 'replace')]/../..//a[text()='修改']")
    # 修改按钮
    delete_button = (By.XPATH, "//*[@id='contentTable']//a[contains(text(), 'replace')]/../..//a[text()='删除']")


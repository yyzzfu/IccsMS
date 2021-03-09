from selenium.webdriver.common.by import By


class TerminalManageLocators:

    # 终端名称
    terminal_name = (By.XPATH, "//*[@id='termName']")
    # 设备型号
    terminal_type = (By.XPATH, "//label[text()='replace']")
    # ip输入框
    terminal_ip = (By.XPATH, "//*[@id='termIp']")
    # 端口输入框
    terminal_port = (By.XPATH, "//*[@id='termPort']")
    # 用户名输入框
    terminal_username = (By.XPATH, "//*[@id='userName']")
    # 密码输入框
    terminal_password = (By.XPATH, "//*[@id='password']")
    # 区域
    area = (By.XPATH, "//label[text()='replace']")
    # 是否推送
    push = (By.XPATH, "//label[text()='replace']")
    # 修改按钮
    modify_button = (By.XPATH, "//*[@id='contentTable']//a[contains(text(),'replace')]/../..//a[text()='修改']")
    # 删除按钮
    delete_button = (By.XPATH, "//*[@id='contentTable']//a[contains(text(),'replace')]/../..//a[text()='删除']")
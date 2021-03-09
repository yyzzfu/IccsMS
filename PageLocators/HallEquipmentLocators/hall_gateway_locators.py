from selenium.webdriver.common.by import By


# 网络通道管理定位元素
class HallGatewayLocators:

    # 网络通道名称输入框
    hall_gateway_name = (By.XPATH, '//*[@id="name"]')
    # ip输入框
    hall_gateway_ip = (By.XPATH, '//*[@id="ip"]')
    # 端口数量输入框
    hall_gateway_port_amount = (By.XPATH, '//*[@id="portAmount"]')
    # 起始端口输入框
    hall_gateway_port_start = (By.XPATH, '//*[@id="portStart"]')
    # 备注输入框
    hall_gateway_remarks = (By.XPATH, '//*[@id="remarks"]')
    # 修改按钮
    modify_button = (By.XPATH, "//*[@id='contentTable']//a[contains(text(),'replace')]/../..//a[text()='修改']")
    # 删除按钮
    delete_button = (By.XPATH, "//*[@id='contentTable']//a[contains(text(),'replace')]/../..//a[text()='删除']")
    # 错误提示信息
    error_tips = (By.XPATH, "//label[text()='replace']/..//label[@class='error']")

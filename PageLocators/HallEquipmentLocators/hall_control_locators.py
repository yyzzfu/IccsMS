from selenium.webdriver.common.by import By


# 测控管理定位元素
class HallControlLocators:

    # 展开网络通道下拉框按钮
    hall_gateway_select = (By.XPATH, '//*[@id="s2id_gatewayId.id"]//b')
    # 需要选择的网络通道
    hall_gateway = (By.XPATH, '//*[@id="select2-drop"]//*[text()="replace"]')
    # 展开网络通道端口按钮
    hall_gateway_port_select = (By.XPATH, '//*[@id="s2id_gatewayPort.id"]//b')
    # 需要选择的网络通道端口
    hall_gateway_port = (By.XPATH, '//*[@id="select2-drop"]//*[contains(text(), "replace")]')
    # 测控名称输入框
    hall_control_name = (By.XPATH, '//*[@id="name"]')
    # 测控通道数输入框
    hall_control_amount = (By.XPATH, '//*[@id="pathwayAmount"]')
    # 测控起始地址输入框
    hall_control_start_address = (By.XPATH, '//*[@id="startAddress"]')
    # 备注输入框
    remarks = (By.XPATH, '//*[@id="remarks"]')
    # 修改按钮
    modify_button = (By.XPATH, "//*[@id='contentTable']//*[contains(text(),'replace')]/../..//a[text()='修改']")
    # 修改按钮
    delete_button = (By.XPATH, "//*[@id='contentTable']//*[contains(text(),'replace')]/../..//a[text()='删除']")


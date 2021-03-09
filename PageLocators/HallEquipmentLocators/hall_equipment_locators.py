from selenium.webdriver.common.by import By


class HallEquipmentLocators:

    # 设备名称输入框
    hall_equipment_name = (By.XPATH, './/*[@id="name"]')
    # 设备类型下拉框展开按钮
    hall_equipment_type_select = (By.XPATH, "//*[@id='s2id_type']//b")
    # 设备类型
    hall_equipment_type = (By.XPATH, '//*[@id="select2-drop"]//*[text()="replace"]')
    # 设备编号
    equipment_code = (By.XPATH, "//*[@id='code']")
    # 协议地址输入框
    protocol_address = (By.XPATH, "//*[@id='address']")
    # 所属区域下拉框展开按钮
    area_select = (By.XPATH, "//*[@id='s2id_area.id']//b")
    # 区域
    # area = (By.XPATH, '//*[@id="select2-drop"]//*[contains(text(),"replace")]//span')
    # area = (By.XPATH, '//*[@id="select2-drop"]//*[text()="replace"]')
    area = (By.XPATH, "//*[@id='select2-drop']//li[1]//div[@class='select2-result-label'][1]")
    # 设备小类下拉框展开按钮
    hall_equipment_child_type_select = (By.XPATH, "//*[@id='s2id_childType']//b")
    # 设备小类输入框
    hall_equipment_child_type_input = (By.XPATH, "//*[@id='select2-drop']//input")
    # mac地址输入框
    mac_address = (By.XPATH, "//*[@id='mac']")
    # 所属区域输入框
    area_input = (By.XPATH, "//*[@id='select2-drop']//input")
    # 备注输入框
    remarks = (By.XPATH, "//*[@id='remarks']")
    # 设备通道--新增按钮
    equipment_gateway_add_button = (By.XPATH, "//*[@id='contentTable']//a")
    # 设备通道下拉框，定位到的是一组值，其中第一个是‘父节点’，第二个是‘父节点端口’，第三个是‘协议’
    equipment_gateway = (By.XPATH, "//*[@id='contentTable']//select")
    # 设备通道--父节点下拉框
    equipment_gateway_parent = (By.XPATH, "//*[@id='hallEquipmentChannelList0_parent']")
    # 设备通道--父节点端口下拉框
    equipment_gateway_parent_port = (By.XPATH, "//*[contains(@id,'parentPort')]")
    # 设备通道--协议下拉框
    equipment_gateway_protocol = (By.XPATH, "//*[contains(@id,'protocolId')]")
    # 修改按钮
    modify_button = (By.XPATH, "//*[@id='contentTable']//*[contains(text(),'replace')]/../..//a[text()='修改']")
    # 修改按钮
    delete_button = (By.XPATH, "//*[@id='contentTable']//*[contains(text(),'replace')]/../..//a[text()='删除']")


from selenium.webdriver.common.by import By


class HallSceneLocators:

    # 场景名称
    hall_scene_name = (By.XPATH, '//*[@id="name"]')
    # 场景说明
    hall_scene_remarks = (By.XPATH, '//*[@id="remarks"]')
    # 添加动作按钮
    add_action_button = (By.XPATH, '//*[@id="contentTable"]//*[text()="添加动作"]')
    # 添加延迟按钮
    add_delay_time_button = (By.XPATH, '//*[@id="contentTable"]//*[text()="添加延迟"]')
    # 添加场景动作--展开设备下拉框
    equipment_select_button = (By.XPATH, '//*[@id="addActionForm"]//*[@id="hallSceneDetail_equipmentId"]/following-sibling::span/child::span/child::span')

    # 添加场景动作--展开执行命令下拉框
    executive_command_button = (By.XPATH, '//*[@id="addActionForm"]//*[@id="hallSceneDetail_commandType"]/following-sibling::span/child::span/child::span')

    # 参数值输入框
    parameter = (By.XPATH, '//*[@id="hallSceneDetail_parameter"]')
    # 添加动作--执行顺序输入框
    action_execute_sequence = (By.XPATH, "//*[@id='hallSceneDetail_executeSeq']")
    # 添加动作中的添加按钮
    add_button_action = (By.XPATH, "//*[@id='hallSceneDetail_btnSubmit']")
    # 添加延迟中的添加按钮
    add_button_delay = (By.XPATH, "//*[@id='hallSceneDelay_btnSubmit']")

    # 设备
    equipment = (By.XPATH, "//span[@class='tree-title' and text()='replace']")
    # 执行命令
    execute_order = (By.XPATH, "//div[@class='combobox-item' and text()='replace']")

    # 延迟
    delay_time = (By.XPATH, "//*[@id='hallSceneDelay_delaySecond']")
    # 添加延迟--执行顺序
    delay_execute_sequence = (By.XPATH, "//*[@id='hallSceneDelay_executeSeq']")

    # 修改按钮
    modify_button = (By.XPATH, "//*[@id='contentTable']//a[contains(text(),'replace')]/../..//a[text()='修改']")
    # 禁用按钮
    disuse_button = (By.XPATH, "//*[@id='contentTable']//a[contains(text(),'replace')]/../..//a[text()='禁用']")
    # 启用按钮
    use_button = (By.XPATH, "//*[@id='contentTable']//a[contains(text(),'replace')]/../..//a[text()='启用']")
    # 删除按钮
    delete_button = (By.XPATH, "//*[@id='contentTable']//a[contains(text(),'replace')]/../..//a[text()='删除']")
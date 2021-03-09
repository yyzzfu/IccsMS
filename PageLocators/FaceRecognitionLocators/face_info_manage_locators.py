from selenium.webdriver.common.by import By


class FaceRecognitionLocators:

    # 姓名
    name = (By.XPATH, "//*[@id='name']")
    # 性别
    gender = (By.XPATH, "//label[text()='replace']")
    # 电话号码
    telephone_number = (By.XPATH, "//*[@id='telNo']")
    # 身份证号码
    id_card_number = (By.XPATH, "//*[@id='idCard']")
    # 单位名称
    company = (By.XPATH, "//*[@id='company']")
    # 人脸照片--选择按钮
    choose_button = (By.XPATH, "//*[@id='faceImageUrlPreview']/following-sibling::a[1]")
    # 人脸照片--清除按钮
    clear_button = (By.XPATH, "//*[@id='faceImageUrlPreview']/following-sibling::a[2]")
    # 智能手表勾选框
    smartwatch = (By.XPATH, "//label[text()='replace']")

    # 员工/访客--添加按钮
    add_button = (By.XPATH, "//*[@id='searchForm']//*[text()='replace']")
    # 员工下拉框展开按钮
    employee_select = (By.XPATH, "//*[@id='s2id_employeeId.id']/a")
    # 员工下拉框中的输入框
    employee_input = (By.XPATH, "//*[@id='select2-drop']//input")
    # 修改按钮
    modify_button = (By.XPATH, "//*[@id='contentTable']//a[contains(text(),'replace')]/../..//a[text()='修改']")
    # 删除按钮
    delete_button = (By.XPATH, "//*[@id='contentTable']//a[contains(text(),'replace')]/../..//a[text()='删除']")

    # -------------------------------------访客等级管理-----------------------------------------------
    # 访客等级管理按钮
    customer_level_manage_button = (By.XPATH, "//*[@id='searchForm']//*[text()='访客等级管理']")
    # 等级按钮
    level_button = (By.XPATH, "//*[@id='contentTable']//a[contains(text(),'customer_replace')]/../..//a[text()='level_replace']")

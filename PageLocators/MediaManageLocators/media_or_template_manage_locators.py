from selenium.webdriver.common.by import By


class MediaTemplateManageLocators:

    # 素材名称
    sucai_name = (By.XPATH, ".//*[@id='name']")
    # 选择按钮
    choice_button = (By.XPATH, "//*[@id='pathPreview']/following-sibling::a[@onclick='pathFinderOpen();']")
    # 素材类型--欢迎词/视频
    sucai_type = (By.XPATH, "//label[text()='replace']")
    # 内容描述
    remarks = (By.XPATH, ".//*[@id='content']")
    # 修改按钮
    modify_button = (By.XPATH, "//*[@id='contentTable']//a[contains(text(),'replace')]/../..//a[text()='修改']")
    # 删除按钮
    delete_button = (By.XPATH, "//*[@id='contentTable']//a[contains(text(),'replace')]/../..//a[text()='删除']")
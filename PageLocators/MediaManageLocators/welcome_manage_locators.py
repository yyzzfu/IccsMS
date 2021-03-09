from selenium.webdriver.common.by import By


class WelcomeManageLocators:

    # 欢迎词素材展开下拉框按钮
    welcome_template_select_button = (By.XPATH, "//*[@id='s2id_mediaId.id']//b")
    # 欢迎词素材下拉框中的输入框
    welcome_template_input = (By.XPATH, "//*[@id='select2-drop']//input")
    # 标题输入框
    title = (By.XPATH, "//*[@id='title']")
    # 内容输入框
    content = (By.XPATH, "//*[@id='content']")
    # 修改按钮
    modify_button = (By.XPATH, "//*[@id='contentTable']//a[contains(text(),'replace')]/../..//a[text()='修改']")
    # 删除按钮
    delete_button = (By.XPATH, "//*[@id='contentTable']//a[contains(text(),'replace')]/../..//a[text()='删除']")
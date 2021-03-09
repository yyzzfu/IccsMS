from PageObjects.basepage import BasePage
from PageLocators.home_page_locators import HomePageLocator as home_loc
from PageLocators.MediaManageLocators.welcome_manage_locators import WelcomeManageLocators as loc


class WelcomeManagePage(BasePage):

    # 编辑欢迎词
    def edit_welcome_word(self, welcome_template, title, content, mode):
        if welcome_template:
            # 展开“欢迎词素材下拉框”
            self.click_element(loc.welcome_template_select_button)
            self.input_text(loc.welcome_template_input, welcome_template)  # 在输入框中输入欢迎词模板名称
            self.enter_button(loc.welcome_template_input)  # 敲击键盘回车键
        if title:
            if mode == '修改':
                self.clear_input(loc.title)
            self.input_text(loc.title, title)
        if content:
            if mode == '修改':
                self.clear_input(loc.content)
            self.input_text(loc.content, content)
        self.click_element(home_loc.submit)

    # 新增欢迎词
    def add_welcome_word(self, welcome_template=None, title=None, content=None):
        self.click_element(home_loc.add_button)
        self.edit_welcome_word(welcome_template, title, content, mode='新增')

    # 修改欢迎词
    def modify_welcome_word(self, welcome_modify, welcome_template=None, title=None, content=None):
        # 点击修改按钮
        modify_button_replace = str(loc.modify_button).replace('replace', welcome_modify)
        self.click_element(eval(modify_button_replace))
        self.edit_welcome_word(welcome_template, title, content, mode='修改')

    # 删除欢迎词
    def delete_welcome_word(self, welcome_delete):
        # 点击删除按钮
        delete_button_replace = str(loc.delete_button).replace('replace', welcome_delete)
        self.click_element(eval(delete_button_replace))
        self.back_to_default_content()
        self.click_element(home_loc.alert_accept_button)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://172.17.46.198:9080/IccsMS')
    LoginPage(driver).login(username='thinkgem', password='admin', code='')
    WelcomeManagePage(driver).add_welcome_word(welcome_template='修改欢迎词模板001', title='欢迎词001', content='欢迎词001')
    # WelcomeManagePage(driver).modify_welcome_word(welcome_modify='欢迎词001', title='修改的欢迎词001', content='修改001')
    # WelcomeManagePage(driver).delete_welcome_word(welcome_delete='修改的欢迎词001')
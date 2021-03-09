from PageObjects.basepage import BasePage
from PageLocators.FaceRecognitionLocators.terminal_manage_locators import TerminalManageLocators as loc
from PageLocators.home_page_locators import HomePageLocator as home_loc


class TerminalManagePage(BasePage):

    # 编辑终端
    def edit_terminal(self, terminal_name, terminal_type, terminal_ip, terminal_port, terminal_username, terminal_password, area, push, mode):
        if terminal_name:
            if mode == '修改':
                self.clear_input(loc.terminal_name)
            self.input_text(loc.terminal_name, terminal_name)
        if terminal_type:
            terminal_type_replace = str(loc.terminal_type).replace('replace', terminal_type)
            self.click_element(eval(terminal_type_replace))
        if terminal_ip:
            if mode == '修改':
                self.clear_input(loc.terminal_ip)
            self.input_text(loc.terminal_ip, terminal_ip)
        if terminal_port:
            if mode == '修改':
                self.clear_input(loc.terminal_port)
            self.input_text(loc.terminal_port, terminal_port)
        if terminal_username:
            if mode == '修改':
                self.clear_input(loc.terminal_username)
            self.input_text(loc.terminal_username, terminal_username)
        if terminal_password:
            if mode == '修改':
                self.clear_input(loc.terminal_password)
            self.input_text(loc.terminal_password, terminal_password)
        if area:
            area_replace = str(loc.area).replace('replace', area)
            self.click_element(eval(area_replace))
        if push:
            push_replace = str(loc.push).replace('replace', push)
            self.click_element(eval(push_replace))
        self.click_element(home_loc.submit)

    # 新增终端
    def add_terminal(self, terminal_name=None, terminal_type=None, terminal_ip=None, terminal_port=None, terminal_username=None,
                     terminal_password=None, area=None, push=None):
        self.click_element(home_loc.add_button)
        self.edit_terminal(terminal_name, terminal_type, terminal_ip, terminal_port, terminal_username, terminal_password, area, push, mode=None)

    # 修改终端
    def modify_terminal(self, terminal_modify, terminal_name=None, terminal_type=None, terminal_ip=None, terminal_port=None, terminal_username=None,
                        terminal_password=None, area=None, push=None):
        # 点击修改按钮
        modify_button_replace = str(loc.modify_button).replace('replace', terminal_modify)
        self.click_element(eval(modify_button_replace))
        self.edit_terminal(terminal_name, terminal_type, terminal_ip, terminal_port, terminal_username, terminal_password, area, push, mode='修改')

    # 删除终端
    def delete_terminal(self, terminal_delete):
        # 点击删除按钮
        delete_button_replace = str(loc.delete_button).replace('replace', terminal_delete)
        self.click_element(eval(delete_button_replace))
        self.back_to_default_content()
        self.click_element(home_loc.alert_accept_button)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://172.17.46.198:9080/IccsMS')
    LoginPage(driver).login(username='thinkgem', password='admin', code='')
    # TerminalManagePage(driver).add_terminal(terminal_name='新增的终端001', terminal_type='巨龙网络摄像头', terminal_ip='127.0.0.1',
    #                                         terminal_port=8888, terminal_username='usrname_test', terminal_password='password_test',
    #                                         area='湖北武汉1', push='否')
    # TerminalManagePage(driver).add_terminal(terminal_name='usb摄像头001', terminal_type='USB摄像头', area='湖北武汉1', push='否')
    TerminalManagePage(driver).delete_terminal(terminal_delete='摄像头001')
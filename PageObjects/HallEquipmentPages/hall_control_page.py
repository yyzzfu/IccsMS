from PageObjects.basepage import BasePage
from PageLocators.HallEquipmentLocators.hall_control_locators import HallControlLocators as loc
from PageLocators.home_page_locators import HomePageLocator as home_loc


class HallControlPage(BasePage):

    # 编辑测控
    def edit_hall_control(self, hall_gateway, hall_gateway_port, hall_control_name, hall_control_amount, hall_control_start_address, remarks, mode):
        if hall_gateway:
            # 展开网络通道下拉框
            self.click_element(loc.hall_gateway_select)
            # 选择网络通道
            hall_gateway_replace = str(loc.hall_gateway).replace('replace', hall_gateway)
            self.click_element(eval(hall_gateway_replace))
        if hall_gateway_port:
            # 展开网络通道端口下拉框
            self.click_element(loc.hall_gateway_port_select)
            # 选择网络通道端口
            hall_gateway_port_replace = str(loc.hall_gateway_port).replace('replace', str(hall_gateway_port))
            self.click_element(eval(hall_gateway_port_replace))
        if hall_control_name:
            if mode == '修改':
                self.clear_input(loc.hall_control_name)
            # 输入测控名称
            self.input_text(loc.hall_control_name, hall_control_name)
        if hall_control_amount:
            if mode == '修改':
                self.clear_input(loc.hall_control_amount)
            # 输入测控通道数
            self.input_text(loc.hall_control_amount, hall_control_amount)
        if hall_control_start_address:
            if mode == '修改':
                self.clear_input(loc.hall_control_start_address)
            # 输入测控起始地址
            self.input_text(loc.hall_control_start_address, hall_control_start_address)
        if remarks:
            if mode == '修改':
                self.clear_input(loc.remarks)
            # 输入备注
            self.input_text(loc.remarks, remarks)
        # 点击保存
        self.click_element(home_loc.submit)

    # 新增测控
    def add_hall_control(self, hall_gateway=None, hall_gateway_port=None, hall_control_name=None, hall_control_amount=None,
                         hall_control_start_address=None, remarks=None):
        # 点击新增按钮
        self.click_element(home_loc.add_button)
        # 在测控编辑界面进行输入
        self.edit_hall_control(hall_gateway, hall_gateway_port, hall_control_name, hall_control_amount, hall_control_start_address, remarks, mode=None)
        return self

    # 修改测控
    def modify_hall_control(self, modify_hall_control, hall_gateway=None, hall_gateway_port=None, hall_control_name=None, hall_control_amount=None,
                            hall_control_start_address=None, remarks=None):
        # 点击修改按钮
        modify_button_replace = str(loc.modify_button).replace('replace', modify_hall_control)
        self.click_element(eval(modify_button_replace))
        # 在测控编辑界面进行输入
        self.edit_hall_control(hall_gateway, hall_gateway_port, hall_control_name, hall_control_amount, hall_control_start_address, remarks, mode='修改')
        return self

    # 删除测控
    def delete_hall_control(self, delete_hall_control):
        # 点击删除按钮
        delete_button_replace = str(loc.delete_button).replace('replace', delete_hall_control)
        self.click_element(eval(delete_button_replace))
        # 返回默认iframe
        self.back_to_default_content()
        # alert中点击确定
        self.click_element(home_loc.alert_accept_button)
        return self


if __name__ == '__main__':
    from PageObjects.start_driver import StartDriver
    home_page = StartDriver.goto_loginPage().login(username='thinkgem', password='admin', code='')
    home_page.goto_hall_control().add_hall_control(hall_gateway='新增网络通道002', hall_gateway_port='1001', hall_control_name='新增的测控001',
                                                   hall_control_amount=5, hall_control_start_address='1000', remarks='新增测试备注001')

    # HallControlPage(driver).modify_hall_control(modify_control='新增的测控001', hall_gateway='修改网络通道002', hall_gateway_port='3001', hall_control_name='修改的测控001',
    #                                             hall_control_amount=1, hall_control_start_address='1111', remarks='修改测试备注001')
    # HallControlPage(driver).delete_hall_control('haha')
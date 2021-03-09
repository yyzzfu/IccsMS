from PageLocators.HallEquipmentLocators.hall_gateway_locators import HallGatewayLocators as loc
from PageObjects.basepage import BasePage
from PageLocators.home_page_locators import HomePageLocator as home_loc


class HallGatewayPage(BasePage):
    # 编辑网络通道
    def edit_hall_gateway(self, name, ip, portAmount, portStart, remarks, mode):
        if name:
            if mode == '修改':
                self.clear_input(loc.hall_gateway_name)
            self.input_text(loc.hall_gateway_name, name)
        if ip:
            if mode == '修改':
                self.clear_input(loc.hall_gateway_ip)
            self.input_text(loc.hall_gateway_ip, ip)
        if portAmount:
            if mode == '修改':
                self.clear_input(loc.hall_gateway_port_amount)
            self.input_text(loc.hall_gateway_port_amount, portAmount)
        if portStart:
            if mode == '修改':
                self.clear_input(loc.hall_gateway_port_start)
            self.input_text(loc.hall_gateway_port_start, portStart)
        if remarks:
            if mode == '修改':
                self.clear_input(loc.hall_gateway_remarks)
            self.input_text(loc.hall_gateway_remarks, remarks)
        # 点击保存按钮
        self.click_element(home_loc.submit)

    # 添加网络通道
    def add_hall_gateway(self, name=None, ip=None, portAmount=None, portStart=None, remarks=None):
        # 点击新增按钮
        self.click_element(home_loc.add_button)
        # 在网络通道编辑界面中进行输入
        self.edit_hall_gateway(name, ip, portAmount, portStart, remarks, mode=None)
        return self

    # 修改网络通道
    def modify_hall_gateway(self, modify_hall_gateway=None, name=None, ip=None, portAmount=None, portStart=None, remarks=None):
        # 点击修改按钮
        modify_button_replace = str(loc.modify_button).replace('replace', modify_hall_gateway)
        self.click_element(eval(modify_button_replace))
        # 在网络通道编辑界面中进行输入
        self.edit_hall_gateway(name, ip, portAmount, portStart, remarks, mode='修改')
        return self

    # 删除网络通道
    def delete_hall_gateway(self, delete_hall_gateway):
        # 点击删除按钮
        delete_button_replace = str(loc.delete_button).replace('replace', delete_hall_gateway)
        self.click_element(eval(delete_button_replace))
        # 返回默认iframe
        self.back_to_default_content()
        # alert中点击确定
        self.click_element(home_loc.alert_accept_button)
        return self


if __name__ == '__main__':
    from PageObjects.start_driver import StartDriver
    home_page = StartDriver.goto_loginPage().login()
    # 新增操作
    a = home_page.goto_hall_gateway().add_hall_gateway(name='12321', ip='172.17.46.108', portAmount=2, portStart=1000, remarks='新增网络通道备注002')
    print(a)
    # HallGatewayPage(driver).modify_hall_gateway(modify_hall_gateway='新增网络通道001', name='修改网络通道002', ip='172.17.46.103',
    #                                             portAmount=3, portStart=3000, remarks='修改网络通道备注002')
    # HallGatewayPage(driver).delete_hall_gateway('修改网络通道001')
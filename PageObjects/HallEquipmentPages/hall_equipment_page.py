from PageObjects.basepage import BasePage
from PageLocators.HallEquipmentLocators.hall_equipment_locators import HallEquipmentLocators as loc
from PageLocators.home_page_locators import HomePageLocator as home_loc


class HallEquimentPage(BasePage):

    # 编辑设备
    def edit_hall_equipment(self, hall_equipment_name, hall_equipment_type, hall_equipment_child_type, mac_address, equipment_code, protocol_address, area,
                            remarks, equipment_gateway_parent, equipment_gateway_parent_port, equipment_gateway_protocol, mode):
        if hall_equipment_name:
            if mode == '修改':
                self.clear_input(loc.hall_equipment_name)
            self.input_text(loc.hall_equipment_name, hall_equipment_name)
        if hall_equipment_type:
            # 展开设备类型下拉框
            self.click_element(loc.hall_equipment_type_select)
            # 选择设备类型
            hall_equipment_type_replace = str(loc.hall_equipment_type).replace('replace', hall_equipment_type)
            self.click_element(eval(hall_equipment_type_replace))
        if hall_equipment_child_type:
            # 展开设备小类下拉框
            self.click_element(loc.hall_equipment_child_type_select)
            # 选择设备小类
            self.input_text(loc.hall_equipment_child_type_input, hall_equipment_child_type)  # 在输入框中输入区域
            self.enter_button(loc.hall_equipment_child_type_input)  # 点击键盘上的回车按键
        if mac_address:
            if mode == '修改':
                self.clear_input(loc.mac_address)
            self.input_text(loc.mac_address, mac_address)
        if equipment_code:
            self.clear_input(loc.equipment_code)
            self.input_text(loc.equipment_code, equipment_code)
        if protocol_address:
            if mode == '修改':
                self.clear_input(loc.protocol_address)
            # 输入协议地址
            self.input_text(loc.protocol_address, protocol_address)
        if area:
            # 展开所属区域下拉框
            self.click_element(loc.area_select)
            # 选择区域
            self.input_text(loc.area_input, area)  # 在输入框中输入区域
            self.enter_button(loc.area_input)    # 点击键盘上的回车按键
        if remarks:
            if mode == '修改':
                self.clear_input(loc.remarks)
            # 输入备注信息
            self.input_text(loc.remarks, remarks)
        if mode == '新增':
            # 在设备通道中点击新增
            self.click_element(loc.equipment_gateway_add_button)
        if equipment_gateway_parent:
            # 在父节点下拉框中选择指定的选项
            self.select(loc.equipment_gateway_parent, equipment_gateway_parent)
        if equipment_gateway_parent_port:
            # 在父节点端口下拉框中选择指定的选项
            self.select(loc.equipment_gateway_parent_port, str(equipment_gateway_parent_port))
        if equipment_gateway_protocol:
            # 在协议下拉框中选择指定的选项
            self.select(loc.equipment_gateway_protocol, equipment_gateway_protocol)
        # 点击保存按钮
        self.click_element(home_loc.submit)

    # 新增设备
    def add_hall_equipment(self, hall_equipment_name=None, hall_equipment_type=None, hall_equipment_child_type=None, mac_address=None, equipment_code=None,
                           protocol_address=None, area=None, remarks=None, equipment_gateway_parent=None, equipment_gateway_parent_port=None,
                           equipment_gateway_protocol=None):
        # 点击新增按钮
        self.click_element(home_loc.add_button)
        # 在编辑设备界面进行输入
        self.edit_hall_equipment(hall_equipment_name, hall_equipment_type, hall_equipment_child_type, mac_address, equipment_code, protocol_address, area, remarks,
                                 equipment_gateway_parent, equipment_gateway_parent_port, equipment_gateway_protocol, mode='新增')
        return self

    # 修改设备
    def modify_hall_equipment(self, modify_hall_equipment, hall_equipment_name=None, hall_equipment_type=None, hall_equipment_child_type=None, mac_address=None,
                              equipment_code=None, protocol_address=None, area=None, remarks=None, equipment_gateway_parent=None, equipment_gateway_parent_port=None,
                              equipment_gateway_protocol=None):
        # 点击修改按钮
        modify_button_replace = str(loc.modify_button).replace('replace', modify_hall_equipment)
        self.click_element(eval(modify_button_replace))
        # 设备名称中输入数据
        self.edit_hall_equipment(hall_equipment_name, hall_equipment_type, hall_equipment_child_type, mac_address, equipment_code, protocol_address, area, remarks,
                                 equipment_gateway_parent, equipment_gateway_parent_port, equipment_gateway_protocol, mode='修改')
        return self

    # 删除设备
    def delete_hall_equipment(self, delete_hall_equipment):
        # 点击删除按钮
        delete_button_replace = str(loc.delete_button).replace('replace', delete_hall_equipment)
        self.click_element(eval(delete_button_replace))
        # 返回默认iframe
        self.back_to_default_content()
        # alert中点击确定
        self.click_element(home_loc.alert_accept_button)
        return self


if __name__ == '__main__':
    from PageObjects.start_driver import StartDriver
    homepage = StartDriver.goto_loginPage().login()
    homepage.goto_hall_equipment().delete_hall_equipment(delete_hall_equipment='新增-窗帘-百叶窗')
    homepage.get_success_delete_tip()
    # HallEquimentPage(driver).add_hall_equipment(hall_equipment_name='新增的设备001', hall_equipment_type='温湿度传感器', protocol_address=100, area='湖北武汉1',
    #                                             remarks='新增设备001', equipment_gateway_parent='新增的测控001', equipment_gateway_parent_port='1001',
    #                                             equipment_gateway_protocol='红外模块')
    # HallEquimentPage(driver).add_hall_equipment(hall_equipment_name='新增的设备002', hall_equipment_type='多媒体屏', hall_equipment_child_type='竖屏',protocol_address=100,
    #                                             area='湖北武汉1', mac_address='68:ED:A4:1C:30:DA',
    #                                             remarks='新增设备002', equipment_gateway_parent='新增的测控001', equipment_gateway_parent_port='1003',
    #                                             equipment_gateway_protocol='红外模块')
    # HallEquimentPage(driver).delete_hall_equipment(delete_hall_equipment='新增的设备002')
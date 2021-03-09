from PageLocators.HallEquipmentLocators.hall_scene_locators import HallSceneLocators as loc
from PageObjects.basepage import BasePage
from PageLocators.home_page_locators import HomePageLocator as home_loc


class HallScenePage(BasePage):

    # 编辑场景
    def edit_hall_scene(self, hall_scene_name, hall_scene_remarks, add_type, equipment, execute_order, parameter, action_execute_sequence,
                        delay_execute_sequence, delay_time, mode):
        if hall_scene_name:
            if mode == '修改':
                self.clear_input(loc.hall_scene_name)
            # 输入场景名称
            self.input_text(loc.hall_scene_name, hall_scene_name)
        if hall_scene_remarks:
            if mode == '修改':
                self.clear_input(loc.hall_scene_remarks)
            # 输入场景说明
            self.input_text(loc.hall_scene_remarks, hall_scene_remarks)
        if mode == '新增':
            if add_type == '添加动作':
                # 点击添加动作按钮
                self.click_element(loc.add_action_button)
            if add_type == '添加延迟':
                # 点击添加延迟按钮
                self.click_element(loc.add_delay_time_button)
        if equipment:
            # 展开设备下拉框
            self.click_element(loc.equipment_select_button)
            equipment_replace = str(loc.equipment).replace('replace', equipment)
            # 点击需要选择的设备
            self.click_element(eval(equipment_replace))
        if execute_order:
            # 展开执行命令下拉框
            self.click_element(loc.executive_command_button)
            execute_order_replace = str(loc.execute_order).replace('replace', execute_order)
            # 点击需要选择的执行命令
            self.click_element(eval(execute_order_replace))
        if parameter:
            if mode == '修改':
                self.clear_input(loc.parameter)
            self.input_text(loc.parameter, parameter)
        if action_execute_sequence:
            self.clear_input(loc.action_execute_sequence)
            # 输入执行顺序
            self.input_text(loc.action_execute_sequence, action_execute_sequence)
        if delay_time:
            if mode == '修改':
                self.clear_input(loc.delay_time)
            self.input_text(loc.delay_time, delay_time)
        if delay_execute_sequence:
            self.clear_input(loc.delay_execute_sequence)
            self.input_text(loc.delay_execute_sequence, delay_execute_sequence)
        if equipment or execute_order or parameter or action_execute_sequence or delay_execute_sequence or delay_time:
            if add_type == '添加动作':
                # 点击添加动作中的添加按钮
                self.click_element(loc.add_button_action)
            elif add_type == '添加延迟':
                # 点击添加延迟中的添加按钮
                self.click_element(loc.add_button_delay)
        # 点击保存按钮
        self.click_element(home_loc.submit)

    # 新增场景
    def add_hall_scene(self, hall_scene_name=None, hall_scene_remarks=None, add_type=None, equipment=None, execute_order=None, parameter=None,
                       action_execute_sequence=None, delay_execute_sequence=None, delay_time=None):
        # 点击新增按钮
        self.click_element(home_loc.add_button)
        # 在场景编辑界面进行输入
        self.edit_hall_scene(hall_scene_name, hall_scene_remarks, add_type, equipment, execute_order, parameter, action_execute_sequence,
                             delay_execute_sequence, delay_time, mode='新增')

    # 修改场景
    def modify_hall_scene(self, modify_hall_scene, hall_scene_name=None, hall_scene_remarks=None, add_type=None, equipment=None, execute_order=None,
                          parameter=None, action_execute_sequence=None, delay_execute_sequence=None, delay_time=None):
        # 点击修改按钮
        modify_button_replace = str(loc.modify_button).replace('replace', modify_hall_scene)
        self.click_element(eval(modify_button_replace))
        # 在场景编辑界面进行输入
        self.edit_hall_scene(hall_scene_name, hall_scene_remarks, add_type, equipment, execute_order, parameter, action_execute_sequence,
                             delay_execute_sequence, delay_time, mode='修改')

    # 禁用场景
    def disuse_hall_scene(self, disuse_hall_scene):
        # 点击禁用按钮
        disuse_button_replace = str(loc.disuse_button).replace('replace', disuse_hall_scene)
        self.click_element(eval(disuse_button_replace))

    # 启用场景
    def use_hall_scene(self, use_hall_scene):
        # 点击启用按钮
        use_button_replace = str(loc.use_button).replace('replace', use_hall_scene)
        self.click_element(eval(use_button_replace))

    # 删除场景
    def delete_hall_scene(self, delete_hall_scene):
        # 点击删除按钮
        delete_button_replace = str(loc.delete_button).replace('replace', delete_hall_scene)
        self.click_element(eval(delete_button_replace))
        # 返回默认iframe
        self.back_to_default_content()
        # alert中点击确定
        self.click_element(home_loc.alert_accept_button)


if __name__ == '__main__':
    from PageObjects.start_driver import StartDriver

    hall_scence = StartDriver.goto_loginPage().login().goto_hall_scence()
    # hall_scence.add_hall_scene(hall_scene_name='新增的场景001', hall_scene_remarks='场景001', add_type='添加动作', equipment='新增-电灯001',
    #                            execute_order='关闭', parameter='000', action_execute_sequence='22')
    # hall_scence.add_hall_scene(hall_scene_name='新增的场景002', hall_scene_remarks='场景002', add_type='添加延迟',
    #                            delay_time=5, delay_execute_sequence=33)
    # HallScenePage(driver).modify_hall_scene(hall_scene_modify='新增的场景001', hall_scene_name='修改的场景001', hall_scene_remarks='修改场景001')
    # HallScenePage(driver).disuse_hall_scene(disuse_hall_scene='修改的场景001')
    # HallScenePage(driver).use_hall_scene(use_hall_scene='修改的场景001')
    # HallScenePage(driver).delete_hall_scene(delete_hall_scene='修改的场景001')
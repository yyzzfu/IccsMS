from PageObjects.basepage import BasePage
from PageLocators.MediaManageLocators.media_or_welcome_play_send_locators import MediaOrWelcomePlaySendLocators as loc
from PageLocators.home_page_locators import HomePageLocator as home_loc


class MediaOrWelcomePlanSendPage(BasePage):

    # 编辑下发计划
    def edit_plan(self, plan_name, sucai, start_date, end_date, start_time, end_time, equipment, mode):
        if plan_name:
            if mode == '修改':
                self.clear_input(loc.plan_name)
            self.input_text(loc.plan_name, plan_name)
        if sucai:
            if mode == '新增':
                # 点击新增按钮
                self.click_element(loc.add_button)
            self.select(loc.sucai_select, sucai)     # 只考虑添加一个素材
        if start_date:
            self.execute_script(self.get_element(loc.start_date))   # 移除日期输入框readonly属性
            self.clear_input(loc.start_date)
            self.input_text(loc.start_date, start_date)
        if end_date:
            self.execute_script(self.get_element(loc.end_date))
            self.clear_input(loc.end_date)
            self.input_text(loc.end_date, end_date)
        if start_time or end_time:            # 只考虑添加一个时间段
            if mode == '新增':
                self.click_element(loc.time_add_button)
            if start_time:
                self.execute_script(self.get_element(loc.start_time))
                self.clear_input(loc.start_time)
                self.input_text(loc.start_time, start_time)
            if end_time:
                self.execute_script(self.get_element(loc.end_time))
                self.clear_input(loc.end_time)
                self.input_text(loc.end_time, end_time)
        if equipment:
            equipment_list = str(equipment).split('|')     # 可勾选多个终端设备
            for i in equipment_list:
                equipment_replace = str(loc.equipment).replace('replace', i)
                self.click_element(eval(equipment_replace))
        self.click_element(home_loc.submit)

    # 新增下发计划
    def add_plan(self, add_type, plan_name=None, sucai=None, start_date=None, end_date=None, start_time=None,
                 end_time=None, equipment=None):
        """
        :param add_type: 新增类型，可输入“视频下发计划添加”或“欢迎词下发计划添加”
        :param plan_name: 任务名称
        :param sucai: 素材名称（仅支持输入一个素材名称）
        :param start_date: 开始日期
        :param end_date: 结束日期
        :param start_time: 开始时间        仅支持添加一个时间段
        :param end_time: 结束时间
        :param equipment: 需要勾选的终端（可输入多个）
        :return:
        """
        video_or_welcome_plan_add_button_replace = str(loc.video_or_welcome_plan_add_button).replace('replace', add_type)
        self.click_element(eval(video_or_welcome_plan_add_button_replace))
        self.edit_plan(plan_name, sucai, start_date, end_date, start_time, end_time, equipment, mode='新增')

    # 修改媒体下发计划
    def modify_plan(self, plan_modify, plan_name=None, sucai=None, start_date=None, end_date=None, start_time=None,
                    end_time=None, equipment=None):
        # 点击修改按钮
        modify_button_replace = str(loc.modify_button).replace('replace', plan_modify)
        self.click_element(eval(modify_button_replace))
        self.edit_plan(plan_name, sucai, start_date, end_date, start_time, end_time, equipment, mode='修改')

    # 删除下发计划
    def delete_plan(self, plan_delete):
        # 点击删除按钮
        delete_button_replace = str(loc.delete_button).replace('replace', plan_delete)
        self.click_element(eval(delete_button_replace))
        self.back_to_default_content()
        self.click_element(home_loc.alert_accept_button)


if __name__ == '__main__':
    from PageObjects.start_driver import StartDriver
    home_page = StartDriver.goto_loginPage().login()
    home_page.goto_media_or_welcome_paln_send().add_plan(
        add_type='视频下发计划添加',
        plan_name='视频下发001',
        sucai='视频素材001',
        start_date='2020-11-30', end_date='2020-11-30',
        start_time='15:30',
        end_time='17:00',
        equipment='多媒体屏'
    )


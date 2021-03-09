from PageObjects.basepage import BasePage
from PageLocators.HallManageLocators.hall_area_bg_manage_locators import HallAreaBgManageLocators as loc
import time
from PageLocators.home_page_locators import HomePageLocator as home_loc


class HallAreaBgManage(BasePage):

    def edit_hall_area_bg(self, dirpath, remarks, mode):
        if dirpath:
            # 获取当前窗口的句柄
            current_window_handle = self.get_current_window_handle()
            time.sleep(1)
            # 点击选择按钮
            self.click_element(loc.select_button)
            # 切换到新打开的窗口
            self.switch_to_new_window(current_window_handle)
            # 上传文件，只需传入指定的目录路径即可（不需指定具体的图片路径），to_upload_file(dirpath)方法会根据目录去找到图片
            from PageObjects.home_page import HomePage
            HomePage().to_upload_file(dirpath)
            time.sleep(2)
            # 切回到默认窗口
            self.back_to_default_window(current_window_handle)
            time.sleep(1)
            # 返回默认iframe
            self.switch_iframe(self.get_element(home_loc.iframe))
        if remarks:
            self.clear_input(loc.remarks)
            # 在备注栏中进行输入
            self.input_text(loc.remarks, remarks)
        # 点击保存按钮
        self.click_element(loc.submit)

    def add_hall_area_bg(self, dirpath=None, remarks=None):
        self.edit_hall_area_bg(dirpath, remarks, mode='新增')

    def modify_hall_area_bg(self, dirpath=None, remarks=None):
        self.edit_hall_area_bg(dirpath, remarks, mode='修改')


if __name__ == '__main__':
    from PageObjects.start_driver import StartDriver

    hall_area_bg = StartDriver.goto_loginPage().login().goto_hall_area_bg_manage()
    dirpath = r"C:\Users\yyzz\Desktop\图片\area_bg\add"
    hall_area_bg.add_hall_area_bg(dirpath=dirpath, remarks='111')
    # HallAreaBgManage(driver).add_hall_area_bg(dirpath=dirpath, remarks='新增001')
    # HallAreaBgManage(driver).modify_hall_area_bg(dirpath=dirpath, remarks='修改001')
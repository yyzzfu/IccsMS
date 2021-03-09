from PageObjects.basepage import BasePage
from PageObjects.home_page import HomePage
from PageLocators.MediaManageLocators.media_or_template_manage_locators import MediaTemplateManageLocators as loc
import time
from PageLocators.home_page_locators import HomePageLocator as home_loc


class SucaiManagePage(BasePage):

    # 编辑素材
    def edit_sucai(self, sucai_name, dirpath, sucai_type, remarks, mode):
        if sucai_name:
            if mode == '修改':
                self.clear_input(loc.sucai_name)
            self.input_text(loc.sucai_name, sucai_name)
        if dirpath:
            # 获取当前窗口的句柄
            current_window_handle = self.get_current_window_handle()
            time.sleep(1)
            self.click_element(loc.choice_button)
            # 切换到新打开的窗口
            self.switch_to_new_window(current_window_handle)
            time.sleep(1.5)
            # 上传文件时，不修改文件的名字，因为欢迎词模板zip文件名必须与zip包内的html文件名一致
            HomePage().to_upload_file_without_modify_filename(dirpath)
            time.sleep(1)
            # 切回到默认窗口
            self.back_to_default_window(current_window_handle)
            time.sleep(1)
            # 返回默认iframe
            self.switch_iframe(self.get_element(home_loc.iframe))
        if sucai_type:
            sucai_type_replace = str(loc.sucai_type).replace('replace', sucai_type)
            self.click_element(eval(sucai_type_replace))
        if remarks:
            if mode == '修改':
                self.clear_input(loc.remarks)
            self.input_text(loc.remarks, remarks)
        self.click_element(home_loc.submit)

        # 新增素材
    def add_sucai(self, sucai_name=None, dirpath=None, sucai_type=None, remarks=None):
        self.click_element(home_loc.add_button)
        self.edit_sucai(sucai_name, dirpath, sucai_type, remarks, mode=None)

    # 修改素材
    def modify_sucai(self, sucai_modify, sucai_name=None, dirpath=None, sucai_type=None, remarks=None):
        # 点击修改按钮
        modify_button_replace = str(loc.modify_button).replace('replace', sucai_modify)
        self.click_element(eval(modify_button_replace))
        # 在素材编辑界面进行输入
        self.edit_sucai(sucai_name, dirpath, sucai_type, remarks, mode='修改')

    # 删除素材
    def delete_sucai(self, sucai_delete):
        # 点击删除按钮
        delete_button_replace = str(loc.delete_button).replace('replace', sucai_delete)
        self.click_element(eval(delete_button_replace))
        self.back_to_default_content()
        self.click_element(home_loc.alert_accept_button)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://172.17.46.198:9080/IccsMS')
    LoginPage(driver).login(username='thinkgem', password='admin', code='')
    dirpath = r"C:\Users\yyzz\Desktop\图片\media\add"
    # dirpath = r"C:\Users\yyzz\Desktop\图片\welcome_template\add"
    # MediaOrTemplateManagePage(driver).add_sucai(sucai_name='欢迎词模板001', dirpath=dirpath, sucai_type='欢迎词', remarks='新增的欢迎词模板001')
    # MediaOrTemplateManagePage(driver).modify_sucai(sucai_modify='欢迎词模板001', sucai_name='修改欢迎词模板001', sucai_type='欢迎词', remarks='修改的欢迎词模板001')
    # MediaOrTemplateManagePage(driver).add_sucai(sucai_name='新增的视频002', dirpath=dirpath, sucai_type='视频', remarks='新增的视频002')
    SucaiManagePage(driver).delete_sucai(sucai_delete='新增的视频002')
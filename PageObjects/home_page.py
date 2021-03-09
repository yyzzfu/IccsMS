from PageObjects.basepage import BasePage
from PageLocators.home_page_locators import HomePageLocator as loc
from Common.my_log import MyLog
import time
from Common import rename_filename_and_get_filepath_locator


class HomePage(BasePage):

    def is_exist_logout_ele(self):
        # 如果元素存在，则返回Ture
        try:
            doc = '首页'
            self.wait_eleVisible(loc.logout_ele, doc=doc)
            return True
        except:
            return False

    def get_home_page_title(self):
        doc = '首页'
        return self.get_title(doc=doc)

    # 判断元素是否存在，存在则返回true，不存在则返回false
    def is_exist_ele(self, locator):
        try:
            # doc = '首页'
            self.wait_eleVisible_without_screen_picture(locator, times=3)
            return True
        except:
            return False

    # 关闭已默认打开的--》网络通道管理tab
    def close_tab_already_opened(self):
        try:
            self.click_element(loc.tab_close)
            MyLog().info('已关闭已默认打开的tab！！！')
        except:
            MyLog().error('关闭已默认打开的tab失败！！！')

    # 切换iframe到新打开的tab里面
    def switch_iframe_to_new_tab(self):
        self.switch_iframe(self.get_element(loc.iframe))

    # ----------------------------------------------进入设备管理下的二级菜单------------------------------------------------------
    # 进入网络通道管理
    def goto_hall_gateway(self):
        try:
            # 点击设备管理一级菜单
            self.click_element(loc.hall_equipment)
            # 点击网络通道管理菜单
            self.click_element(loc.hall_gateway)
            # 切换iframe到新打开的tab里面
            self.switch_iframe_to_new_tab()
            MyLog().info('已进入网络通道管理界面！！！')
            from PageObjects.HallEquipmentPages.hall_gateway_page import HallGatewayPage
            return HallGatewayPage()
        except:
            MyLog().error('进入网络通道管理界面失败！！！')

    # 进入测控管理
    def goto_hall_control(self):
        try:
            # 关闭已默认打开的tab
            self.close_tab_already_opened()
            # 点击设备管理一级菜单
            self.click_element(loc.hall_equipment)
            # 点击测控管理菜单
            self.click_element(loc.hall_control)
            self.switch_iframe_to_new_tab()
            MyLog().info('已进入测控管理界面！！！')
            from PageObjects.HallEquipmentPages.hall_control_page import HallControlPage
            return HallControlPage()
        except:
            MyLog().error('进入测控管理界面失败！！！')

    # 进入设备管理
    def goto_hall_equipment(self):
        try:
            # 关闭已默认打开的tab
            self.close_tab_already_opened()
            # 点击设备管理一级菜单
            self.click_element(loc.hall_equipment)
            # 点击设备管理二级菜单
            self.click_element(loc.hall_equipment_2)
            self.switch_iframe_to_new_tab()
            MyLog().info('已进入设备管理界面！！！')
            from PageObjects.HallEquipmentPages.hall_equipment_page import HallEquimentPage
            return HallEquimentPage()
        except:
            MyLog().error('进入设备管理界面失败！！！')

    # 进入场景设置
    def goto_hall_scence(self):
        try:
            # 关闭已默认打开的tab
            self.close_tab_already_opened()
            # 点击设备管理一级菜单
            self.click_element(loc.hall_equipment)
            # 点击场景设置二级菜单
            self.click_element(loc.hall_scene)
            self.switch_iframe_to_new_tab()
            self.log.info('已进入场景设置界面！！！')
            from PageObjects.HallEquipmentPages.hall_scene_page import HallScenePage
            return HallScenePage()
        except:
            self.log.error('进入场景设置界面失败！！！')

    # -----------------------------------------------------进入营业厅管理下的二级菜单-----------------------------
    # 进入区域管理
    def goto_hall_area_manage(self):
        try:
            # 关闭已默认打开的tab
            self.close_tab_already_opened()
            # 点击营业厅管理一级菜单
            self.click_element(loc.hall_manage)
            # 点击区域管理
            self.click_element(loc.hall_area_manage)
            self.switch_iframe_to_new_tab()
            self.log.info('已经进入区域管理设置界面！！！')
            from PageObjects.HallManagePages.hall_area_manage_page import HallAreaManagePage
            return HallAreaManagePage()
        except:
            self.log.error('进入区域管理设置界面失败！！！')

    # 进入区域分布图管理
    def goto_hall_area_bg_manage(self):
        try:
            # 关闭已默认打开的tab
            self.close_tab_already_opened()
            # 点击营业厅管理一级菜单
            self.click_element(loc.hall_manage)
            # 点击区域分布图管理
            self.click_element(loc.hall_area_bg_manage)
            self.switch_iframe_to_new_tab()
            self.log.info('已经进入区域分布图管理界面！！！')
            from PageObjects.HallManagePages.hall_area_bg_manage_page import HallAreaBgManage
            return HallAreaBgManage()
        except:
            self.log.error('进入区域分布图管理界面失败！！！')

    # -----------------------------------------------------进入人脸识别下的二级菜单-----------------------------
    # 进入人脸信息管理
    def goto_face_info_manage(self):
        try:
            # 关闭已默认打开的tab
            self.close_tab_already_opened()
            # 点击人脸识别一级菜单
            self.click_element(loc.face_recognition)
            # 点击人脸信息管理
            self.click_element(loc.face_info_manage)
            self.switch_iframe_to_new_tab()
            self.log.info('已经进入人脸信息管理界面！！！')
            from PageObjects.FaceRecognitionPages.face_info_manage_page import FaceRecognitionPage
            return FaceRecognitionPage()
        except:
            self.log.error('进入人脸信息管理界面失败！！！')

    # 进入终端管理
    def goto_terminal_manage(self):
        try:
            # 关闭已默认打开的tab
            self.close_tab_already_opened()
            # 点击人脸识别一级菜单
            self.click_element(loc.face_recognition)
            # 点击终端管理
            self.click_element(loc.terminal_manage)
            self.switch_iframe_to_new_tab()
            self.log.info('已经进入终端管理界面！！！')
            from PageObjects.FaceRecognitionPages.terminal_manage_page import TerminalManagePage
            return TerminalManagePage()
        except:
            self.log.error('进入终端管理界面失败！！！')

    # -----------------------------------------------------进入媒体管理下的二级菜单-----------------------------
    # 进入媒体素材管理
    def goto_sucai_manage(self):
        try:
            # 关闭已默认打开的tab
            self.close_tab_already_opened()
            # 点击媒体一级菜单
            self.click_element(loc.media_manage)
            # 点击媒体素材管理
            self.click_element(loc.media_or_template_manage)
            self.switch_iframe_to_new_tab()
            self.log.info('已经进入媒体素材管理界面！！！')
            from PageObjects.MediaManagePages.sucai_manage_page import SucaiManagePage
            return SucaiManagePage()
        except:
            self.log.error('进入媒体素材管理界面失败！！！')

    # 进入媒体下发计划
    def goto_media_or_welcome_paln_send(self):
        try:
            # 关闭已默认打开的tab
            self.close_tab_already_opened()
            # 点击媒体管理一级菜单
            self.click_element(loc.media_manage)
            # 点击媒体下发计划
            self.click_element(loc.media_or_welcome_play_send)
            self.switch_iframe_to_new_tab()
            self.log.info('已经进入媒体下发计划界面！！！')
            from PageObjects.MediaManagePages.media_or_welcome_plan_send_pages import MediaOrWelcomePlanSendPage
            return MediaOrWelcomePlanSendPage()
        except:
            self.log.error('进入媒体下发计划界面失败！！！')

    # 进入欢迎词管理
    def goto_welcome_manage(self):
        try:
            # 关闭已默认打开的tab
            self.close_tab_already_opened()
            # 点击媒体管理一级菜单
            self.click_element(loc.media_manage)
            # 点击欢迎词管理
            self.click_element(loc.welcome_manage)
            self.switch_iframe_to_new_tab()
            self.log.info('已经进入欢迎词管理界面！！！')
            from PageObjects.MediaManagePages.welcome_manage_pages import WelcomeManagePage
            return WelcomeManagePage()
        except:
            self.log.error('进入欢迎词管理界面失败！！！')

    def get_success_save_tip(self):
        try:
            tip = self.get_text(loc.success_save_tip)
            self.log.info('获取提示信息成功！！！获取到的文本信息为{}'.format(tip))
            return tip
        except:
            self.log.info('获取提示信息失败！！！')

    def get_success_delete_tip(self):
        time.sleep(0.5)                   # 睡眠0.5秒，待删除成功后，再进行获取提示信息操作
        self.switch_iframe_to_new_tab()   # iframe切换，不然删除成功后，不能获取到删除成功提示信息
        try:
            tip = self.get_text(loc.success_save_tip)
            self.log.info('获取提示信息成功！！！获取到的文本信息为{}'.format(tip))
            return tip
        except:
            self.log.info('获取提示信息失败！！！')

    def get_hall_area_bg_success_save_tip(self):
        try:
            tip = self.get_text(loc.hall_area_bg_success_save_tip)
            self.log.info('获取区域分布图保存成功提示信息成功！！！获取到的文本信息为{}'.format(tip))
            return tip
        except:
            self.log.info('获取区域分布图保存成功提示信息失败！！！')

    # 在打开的窗口中上传文件，并选择第一个文件后，点击保存按钮
    def to_upload_file(self, dirpath, file_type='.jpg'):
        # 切换到iframe
        self.switch_iframe(self.get_element(loc.upload_iframe))
        # 点击上传按钮
        self.click_element(loc.upload_button)
        # 修改照片名称
        locator_and_path = rename_filename_and_get_filepath_locator.get_file_locator_and_path(dirpath, file_type)
        time.sleep(2)
        # 调用BasePage中的upload方法，传入文件
        self.upload(locator_and_path[1])
        # 加入time睡眠几秒
        time.sleep(2)
        # 双击已上传的图片
        self.double_click(locator_and_path[0])
        time.sleep(1)

    def to_upload_file_without_modify_filename(self, dirpath):
        # 切换到iframe
        self.switch_iframe(self.get_element(loc.upload_iframe))
        # 点击上传按钮
        self.click_element(loc.upload_button)
        # 修改照片名称
        locator_and_path = rename_filename_and_get_filepath_locator.get_file_locator_and_path_without_modify_filename(dirpath)
        time.sleep(2)
        # 调用BasePage中的upload方法，传入文件
        self.upload(locator_and_path[1])
        # 加入time睡眠几秒
        time.sleep(2)
        # 双击已上传的图片
        self.double_click(locator_and_path[0])
        time.sleep(1)


if __name__ == '__main__':
    from PageObjects.start_driver import StartDriver

    StartDriver.goto_loginPage().login('thinkgem', 'admin').goto_hall_equipment()


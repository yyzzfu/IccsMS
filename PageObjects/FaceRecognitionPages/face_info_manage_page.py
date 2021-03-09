from PageObjects.basepage import BasePage
from PageLocators.FaceRecognitionLocators.face_info_manage_locators import FaceRecognitionLocators as loc
from PageObjects.home_page import HomePage
from PageLocators.home_page_locators import HomePageLocator as home_loc
import time


class FaceRecognitionPage(BasePage):

    # 编辑人脸信息
    def edit_face_info(self, employee, name, gender, telephone_number, id_card_number, company, dirpath, smartwatch, mode):
        if employee:
            # 展开员工下拉框
            self.click_element(loc.employee_select)
            # 选择员工
            self.input_text(loc.employee_input, employee)  # 在员工下拉框--输入框中输入员工名称
            self.enter_button(loc.employee_input)  # 敲击键盘上的回车键
        if name:
            if mode == '修改':
                self.clear_input(loc.name)
        # 输入姓名
            self.input_text(loc.name, name)
        if gender:
            # 选择性别
            gender_replace = str(loc.gender).replace('replace', gender)
            self.click_element(eval(gender_replace))
        if telephone_number:
            self.clear_input(loc.telephone_number)
            # 输入电话号码
            self.input_text(loc.telephone_number, telephone_number)
        if id_card_number:
            if mode == '修改':
                self.clear_input(loc.id_card_number)
            # 输入身份证号码
            self.input_text(loc.id_card_number, id_card_number)
        if company:
            if mode == '修改':
                self.clear_input(loc.company)
            # 输入单位名称
            self.input_text(loc.company, company)
        if dirpath:
            # 获取当前窗口的句柄
            current_window_handle = self.get_current_window_handle()
            time.sleep(1)
            # 人脸照片栏中，点击选择按钮
            self.click_element(loc.choose_button)
            # 切换到新打开的窗口
            self.switch_to_new_window(current_window_handle)
            HomePage().to_upload_file(dirpath)
            time.sleep(2)
            # 切回到默认窗口
            self.back_to_default_window(current_window_handle)
            time.sleep(1)
            # 返回默认iframe
            self.switch_iframe(self.get_element(home_loc.iframe))
        if smartwatch:
            smartwatch_list = str(smartwatch).split('|')
            for i in smartwatch_list:
                smartwatch_replace = str(loc.smartwatch).replace('replace', i)
                # 勾选智能手表
                self.click_element(eval(smartwatch_replace))
        # 点击保存按钮
        self.click_element(home_loc.submit)

        # 新增人脸信息
    def add_face_info(self, add_type, employee=None, name=None, gender=None, telephone_number=None, id_card_number=None,
                      company=None, dirpath=None, smartwatch=None):
        """
        :param add_type: 添加按钮的类型，可输入“访客添加”或“员工添加”
        :param employee: 员工姓名             与访客姓名二选一，只能输入一个
        :param name: 访客姓名                 与员工姓名二选一，只能输入一个
        :param gender: 性别，可输入“男”或“女”
        :param telephone_number: 电话号码
        :param id_card_number: 身份证号码
        :param company: 单位名称
        :param dirpath: 人脸照片存放的文件夹
        :param smartwatch: 需要勾选的智能提醒设备
        :return:
        """
        # 点击添加按钮
        add_button_replace = str(loc.add_button).replace('replace', add_type)
        self.click_element(eval(add_button_replace))
        # 在人脸信息编辑界面进行输入
        self.edit_face_info(employee, name, gender, telephone_number, id_card_number, company, dirpath, smartwatch, mode=None)

    # 修改人脸信息
    def modify_face_info(self, modify_face_info, employee=None, name=None, gender=None, telephone_number=None, id_card_number=None,
                         company=None, dirpath=None, smartwatch=None):
        # 点击删除按钮
        modify_button_replace = str(loc.modify_button).replace('replace', modify_face_info)
        self.click_element(eval(modify_button_replace))
        self.edit_face_info(employee, name, gender, telephone_number, id_card_number, company, dirpath, smartwatch, mode='修改')

    # 删除人脸信息
    def delete_face_info(self, delete_face_info):
        # 点击删除按钮
        delete_button_replace = str(loc.delete_button).replace('replace', delete_face_info)
        self.click_element(eval(delete_button_replace))
        # 返回默认iframe
        self.back_to_default_content()
        # alert中点击确定
        self.click_element(home_loc.alert_accept_button)

    # 访客等级管理
    def set_customer_level(self, customer, level):
        # 点击访客等级管理按钮
        self.click_element(loc.customer_level_manage_button)
        # 在操作栏中点击等级按钮
        level_button_replace = str(loc.level_button).replace('customer_replace', customer).replace('level_replace', level.lower())
        self.click_element(eval(level_button_replace))
        # 返回默认iframe
        self.back_to_default_content()
        # 在弹出的提示框中点击确认
        self.click_element(home_loc.alert_accept_button)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://172.17.46.198:9080/IccsMS')
    LoginPage(driver).login(username='thinkgem', password='admin', code='')
    dirpath = r'C:\Users\yyzz\Desktop\图片\face\customer_modify'
    # FaceRecognitionPage(driver).add_face_info(add_type='访客添加', name='访客001', gender="男", telephone_number='15973177566',
    #                                           company='武汉精伦电气', dirpath=dirpath, smartwatch='智能手表')
    # FaceRecognitionPage(driver).add_face_info(add_type='员工添加', employee='系统管理员', gender='女', id_card_number=421023198902010120,
    #                                           dirpath=dirpath, smartwatch='智能手表')
    # FaceRecognitionPage(driver).modify_face_info(modify_face_info='员工', employee='测试', gender='女', telephone_number=15974511555, smartwatch='智能手表')
    # FaceRecognitionPage(driver).delete_face_info(delete_face_info='员工')
    # FaceRecognitionPage(driver).set_customer_level(customer='访客', level='黑名单')
    # FaceRecognitionPage(driver).set_customer_level(customer='访客', level='白名单')
    FaceRecognitionPage(driver).set_customer_level(customer='访客', level='vip')
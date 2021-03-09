from PageObjects.basepage import BasePage
from PageLocators.HallManageLocators.hall_area_manage_locators import HallAreaManageLocators as loc
from PageLocators.home_page_locators import HomePageLocator as home_loc


class HallAreaManagePage(BasePage):

    def edit_hall_area(self, hall_area_name, mode):
        if hall_area_name:
            if mode == '修改':
                self.clear_input(loc.hall_area_name)
            # 在输入框中进行输入
            self.input_text(loc.hall_area_name, hall_area_name)
        # 点击保存按钮
        self.click_element(home_loc.submit)

    def add_hall_area(self, hall_area_name=None):
        # 点击新增按钮
        self.click_element(home_loc.add_button)
        self.edit_hall_area(hall_area_name, mode='新增')

    def modify_hall_area(self, hall_area_modify, hall_area_name=None):
        # 点击修改按钮
        modify_button_replace = str(loc.modify_button).replace('replace', hall_area_modify)
        self.click_element(eval(modify_button_replace))
        self.edit_hall_area(hall_area_name, mode='修改')

    def delete_hall_area(self, hall_area_delete):
        # 点击删除按钮
        delete_button_replace = str(loc.delete_button).replace('replace', hall_area_delete)
        self.click_element(eval(delete_button_replace))
        # 返回默认iframe
        self.back_to_default_content()
        # alert中点击确定
        self.click_element(home_loc.alert_accept_button)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://172.17.46.196:8080/IccsMS')
    LoginPage(driver).login(username='thinkgem', password='admin', code='')
    # HallAreaManagePage(driver).add_hall_area(hall_area_name='新增场景001')
    # HallAreaManagePage(driver).modify_hall_area(hall_area_modify='新增场景001', hall_area_name='修改场景001')
    HallAreaManagePage(driver).delete_hall_area(hall_area_delete='修改场景001')


import time
import re
from PageLocators.login_page_locators import LoginPageLocator as loc
from PageObjects.basepage import BasePage
from aip import AipOcr
from PIL import Image
from Common import dir_path
from PageObjects.home_page import HomePage

""" 你的 APPID AK SK """
config = {
    "appId": '20367335',
    "apiKey": 'wfXUvEBDyQT87der31X0i6L6',
    "secretKey": 'WeCD7QoGG4oIRrZrWFAv1Gaig05KqbM4'
}

client = AipOcr(**config)


class LoginPage(BasePage):

    def login(self, username='thinkgem', password='admin', code=''):
        doc = '登录页面_登录操作'
        if username:
            self.input_text(loc.username_ele, username, doc=doc)
        if password:
            self.input_text(loc.password_ele, password, doc=doc)
        if code:
            self.input_text(loc.code_ele, code, doc=doc)
        # 手动输入验证码
        while True:
            time.sleep(10)
            if self.get_title() == '电力营业厅智能中控系统 登录':
                self.click_element(loc.click_button)
                time.sleep(0.5)
                if self.get_title() == '电力营业厅智能中控系统 登录':
                    self.clear_input(loc.code_ele)
                elif self.get_title() == '电力营业厅智能中控系统':
                    break
            elif self.get_title() == '电力营业厅智能中控系统':
                break
        return HomePage()

    def clear_username_input(self):
        doc = '登录页面'
        self.wait_eleVisible(loc.username_ele, doc=doc)
        self.clear_input(loc.username_ele, doc=doc)
        return self

    def clear_password_input(self):
        doc = '登录页面'
        self.wait_eleVisible(loc.password_ele, doc=doc)
        self.clear_input(loc.password_ele, doc=doc)
        return self

    def clear_code_input(self):
        doc = '登录页面'
        self.wait_eleVisible(loc.code_ele, doc=doc)
        self.clear_input(loc.code_ele, doc=doc)
        return self

    def code_image_to_text(self, file_name=None):
        if file_name is None:
            file_name = dir_path.code_picture_dir + "/code.png"
        self.driver.save_screenshot(file_name)
        code_element = self.driver.find_element_by_xpath('//*[@class="mid validateCode"]')
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width'] + left
        height = code_element.size['height'] + top
        im = Image.open(file_name)
        img = im.crop((left, top, right, height))
        img.save(file_name)
        img = Image.open(file_name)
        # 模式"L"为灰色图像
        img = img.convert('L')
        img.save(file_name)
        text = self.get_image_str(file_name)
        code_text = (re.findall(r'[a-zA-Z0-9]', text))
        text = ''.join(code_text)
        return text

    """ 读取图片 """
    def get_file_content(self, file_name):
        with open(file_name, 'rb') as fp:
            return fp.read()

    def get_image_str(self, file_name):
        image = self.get_file_content(file_name)
        """ 调用通用文字识别, 图片参数为本地图片 """
        result = client.basicGeneral(image)
    # 结果拼接返回输出
        if 'words_result' in result:
            return ''.join([w['words'] for w in result['words_result']])

    # 刷新页面
    def refresh_page(self):
        self.driver.refresh()
        return self


if __name__ == '__main__':
    from PageObjects.start_driver import StartDriver
    StartDriver.goto_loginPage().login('thinkgem', 'admin')

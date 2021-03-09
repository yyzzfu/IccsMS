# from PageObjects.login_page import LoginPage
# from selenium import webdriver
from Common.my_log import MyLog

#
# def login_sucess(driver):
#     lg = LoginPage(driver)
#     code = lg.code_image_to_text()
#     # self.lg.login(LD.sucess_data['username'], LD.sucess_data['password'], LD.sucess_data['code'])
#     lg.login(LD.sucess_data['username'], LD.sucess_data['password'], code)
#     if lg.get_title() != '电力营业厅智能中控系统':
#         MyLog().info('登录失败！！！')
#         lg.clear_username_input()
#         lg.clear_password_input()
#         lg.clear_code_input()
#         lg.refresh_page()
#         login_sucess(driver)
#     else:
#         MyLog().info('登录成功！！！')


# if __name__ == '__main__':
    # driver = webdriver.Firefox()
    # driver.get('http://172.17.46.198:9080/IccsMS')
    # login_sucess(driver)

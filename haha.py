import time
import os
import random

# print(time.asctime())
# print(time.time())
# print(time.localtime())
# print(type(time.localtime()))
# a = time.localtime(time.time() - 60*60*24*2)
# b = time.strftime("%Y:%m-%d %H-%M-%S", a)
# print(b)
# print(time.strftime("%Y:%m-%d %H-%M-%S"))
# print(os.getcwd())
# print(os.path.exists('TestCases'))
# print('fafa'      'fasf')
# a = range(0, 101)
# print(a.__class__)
# print(type(a))
# print(a)
# for i in a:
#     print(i)

# for i in range(1, 101):
#     if i in [20, 21]:
#         # continue
#         break
#     print(i)
# computer_num = random.randint(1, 100)
# while True:
#     b = int(input("请输入一个整数："))
#     if computer_num == b:
#         print('猜对了!!!')
#         break
#     elif computer_num > b:
#         print('大一点！！！')
#     elif computer_num < b:
#         print('小一点！！！')
# #
# def mm(a, b, c):
#     print(a)
#     print(b)
#     print(c)
#
# d = {'a':1, 'b':2 ,'c':3}
# mm(**d)
#
# a = [i*i for i in range(1, 10)]
# print(a)
# a = []
# for i in range(1, 10):
#     b = i*i
#     a.append(b)
# print(a)

# a = []
# for i in range(1, 5):
#     for j in range(1, 5):
#         a.append(i*j)
# print(a)
# from appium.webdriver.common.touch_action import TouchAction
from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By


# option = webdriver.ChromeOptions()
# option.add_experimental_option('w3c', False)
driver = webdriver.Chrome()
driver.get('https://image.baidu.com/')
driver.implicitly_wait(5)
driver.maximize_window()
driver.find_element(By.ID, 'stTipsBox').click()
driver.find_element(By.ID, 'stfile').send_keys(r'C:\Users\yyzz\Desktop\图片\微信图片.jpg')
# print(driver.current_window_handle)
# print(driver.window_handles)
# driver.switch_to.frame()
# driver.switch_to_default_content()
# driver.switch_to.parent_frame()
# driver.sw
# input_ele = driver.find_element(By.ID, 'kw')
# input_ele.send_keys('haha')
# driver.find_element(By.ID, 'su').click()
# action = TouchActions(driver)
# action.scroll_from_element(input_ele, 0, 10000)
# action.perform()
a = driver.switch_to_alert().send_keys()

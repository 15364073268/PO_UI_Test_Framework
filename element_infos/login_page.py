#coding=gbk
from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from common.log_utils import logger
from common.base_page import BasePage

from common.element_data_utils import ExeclRead


class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        """��һ��"""
        # self.username_inputbox={'element_name':'�û��������',
        #                         'locator_type':'xpath',
        #                         'locator_value':'//input[@id="account"]',
        #                         'timeout':2}
        # self.password_inputbox = {'element_name': '�û��������',
        #                           'locator_type': 'xpath',
        #                           'locator_value': '//input[@name="password"]',
        #                           'timeout': 2}
        # self.login_button = {'element_name': '�û��������',
        #                           'locator_type': 'xpath',
        #                           'locator_value': '//button[@id="submit"]',
        #                           'timeout': 2}
        '''�ڶ���'''
        self.element_read = ExeclRead('login_page').execl_element_read()
        self.username_inputbox = self.element_read['username_inputbox']
        self.password_inputbox = self.element_read['password_inputbox']
        self.login_button = self.element_read['login_button']

    def input_username(self,username):
        self.input_message(self.username_inputbox,username)

    def input_password(self,password):
        self.input_message(self.password_inputbox,password)

    def click_login(self):
        self.ui_click(self.login_button)



if __name__ == '__main__':
    now_path = os.path.dirname(__file__)
    driver_path = os.path.join(now_path, '../webdriver/chromedriver')
    driver = webdriver.Chrome(executable_path=driver_path)
    logginer = LoginPage(driver)
    logginer.get_open('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
    logginer.input_username('test01')
    logginer.input_password('newdream123')
    logginer.click_login()

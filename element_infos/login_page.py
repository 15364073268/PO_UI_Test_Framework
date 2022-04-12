#coding=gbk
from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from common.log_utils import logger


now_path = os.path.dirname(__file__)
driver_path = os.path.join(now_path,'../webdriver/chromedriver')


class LoginPage:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
        self.user_inputbox = self.driver.find_element(By.XPATH, '//input[@id="account"]')
        self.password_inputbox = self.driver.find_element(By.XPATH, '//input[@name="password"]')
        self.login_button = self.driver.find_element(By.XPATH, '//button[@id="submit"]')

    def input_username(self,username):
        self.user_inputbox.send_keys(username)
        logger.info('用户名输入:'+str(username))

    def input_password(self,password):
        self.password_inputbox.send_keys(password)
        logger.info('密码输入:' + str(password))

    def click_login(self):
        self.login_button.click()
        logger.info('点击登录')


if __name__ == '__main__':
    login_page = LoginPage()
    login_page.input_username('test01')
    login_page.input_password('newdream123')
    login_page.click_login()
#coding=gbk
from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from element_infos import login_page
from common.log_utils import logger




class MainPage:
    def __init__(self):
        loginer = login_page.LoginPage()
        loginer.input_username('test01')
        loginer.input_password('newdream123')
        loginer.click_login()
        self.driver = loginer.driver
        self.my_menu = self.driver.find_element(By.XPATH, '//*[@id="navbar"]/ul/li[1]/a/span')
        self.product_menu = self.driver.find_element(By.XPATH, '//*[@id="navbar"]/ul/li[2]/a')
        self.companyname_show = self.driver.find_element(By.XPATH, '//*[@id="companyname"]')
        self.username_showspan = self.driver.find_element(By.XPATH, '//*[@id="userNav"]/li/a/span[1]')

    def get_company(self):
        value = self.companyname_show.get_attribute('title')
        logger.info('查看公司:'+ str(value))
        return value

    def goto_my(self):
        self.my_menu.click()

    def goto_product(self):
        self.product_menu.click()

    def get_username(self):
        value = self.username_showspan.text
        return value



if __name__ == '__main__':
    mainpage = MainPage()
    logger.info(mainpage.get_company())
#coding=gbk
from selenium import webdriver
from common.log_utils import logger
from selenium.webdriver.common.by import By
import time


class BasePage():
    def __init__(self,driver):
        self.driver = driver

    def get_open(self,url):
        self.driver.get(url)
        logger.info('浏览器打开网页:{}'.format(url))

    def window_max(self):
        self.driver.maximize_window()
        logger.info('浏览器最大化')

    def find1_element(self,element_dir):
        element_name = element_dir['element_name']
        locator_type = element_dir['locator_type']
        locator_value = element_dir['locator_value']
        timeout = element_dir['timeout']
        if locator_type == 'id':
            locator_type = By.ID
        elif locator_type == 'xpath':
            locator_type = By.XPATH
        elif locator_type == 'css':
            locator_type = By.CSS_SELECTOR

        element = self.driver.find_element(locator_type,locator_value)
        logger.info('通过{}方式，定位信息{}执行'.format(timeout,locator_value))
        time.sleep(timeout)
        logger.info('等待{}秒'.format(timeout))
        return element

    def input_message(self,element_dir,massage):
        self.find1_element(element_dir).send_keys(massage)
        logger.info('填入信息{}'.format(massage))

    def ui_click(self,element_dir):
        self.find1_element(element_dir).click()
        logger.info('触发点击')






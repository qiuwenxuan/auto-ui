from selenium.webdriver.common.by import By

from common.logger import logger
from common.utils import xpath_tuple


class Event(object):

    def login(self, driver, username, password):
        # 输入账户和密码
        ele_send_key(driver, xpath_tuple('//*[@placeholder="请输入用户名"]'), username)
        ele_send_key(driver, xpath_tuple('//*[@placeholder="请输入密码"]'), password)
        logger.info(f"输入账户和密码username:【{username}】 password:【{password}】")

        # 点击登录
        ele_click(driver, (By.XPATH, '//input[@value="登录"]'))

    def register(self, username, password, email, open_page):
        # 获取驱动
        driver = open_page
        # 点击立即注册
        ele_click(driver, xpath_tuple('//a[@href|text()="立即注册"]'))
        # 输入注册信息
        ele_send_key(driver, xpath_tuple('//label[contains(text(),"用户名")]/following-sibling::*[1]'), username)
        ele_send_key(driver, xpath_tuple('//label[contains(text(),"密码")]/following-sibling::*[1]'), password)
        ele_send_key(driver, xpath_tuple('//label[contains(text(),"确认密码")]/following-sibling::*[1]'), password)
        ele_send_key(driver, xpath_tuple('//label[contains(text(),"邮箱")]/following-sibling::*[1]'), email)
        # 点击注册按钮
        ele_click(driver, xpath_tuple('//*[@class="reg_sub"]/*[@value="注 册"]'))

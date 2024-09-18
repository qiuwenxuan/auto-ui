import re
from time import sleep

import allure
from selenium import webdriver
from selenium.common import TimeoutException, NoAlertPresentException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait as WD

from common.logger import LoggerManager
from config.conf import CHROME_PATH


class BasePage:
    logger = LoggerManager().get_logger()

    def __init__(self, driver, timeout=30):
        self.driver = driver
        self.outTime = timeout

        self.byDict = {
            'id': By.ID,
            'name': By.NAME,
            'class_name': By.CLASS_NAME,
            'xpath': By.XPATH,
            'link_text': By.LINK_TEXT
        }

    @allure.step('页面寻找单个元素')
    def find_element(self, by, locator):
        self.logger.info(f'----------页面寻找单个元素：{locator}----------')
        try:
            element = WD(self.driver, self.outTime).until(lambda x: x.find_element(self.byDict[by], locator))
            self.logger.info(f'页面元素被找到')
        except TimeoutException as t:
            self.logger.error(f'寻找单个元素超时,异常为:{t}')
            raise t
        else:
            return element

    @allure.step('页面寻找多个元素')
    def find_elements(self, by, locator):
        self.logger.info(f'----------页面寻找多个元素：{locator}----------')
        try:
            element = WD(self.driver, self.outTime).until(lambda x: x.find_elements(self.byDict[by], locator))
            self.logger.info(f'多个元素被找到')
        except TimeoutException as t:
            self.logger.error(f'寻找多个元素超时,异常为：{t}')
            raise t
        else:
            return element

    @allure.step('判断元素是否可见')
    def is_element_visible(self, by, locator):
        self.logger.info(f'----------判断元素是否可见：{locator}----------')
        try:
            WD(self.driver, self.outTime).until(EC.visibility_of_element_located((self.byDict[by], locator)))
            self.logger.info(f'元素可见')
        except TimeoutException:
            self.logger.info(f'元素不可见')
            return False
        else:
            return True

    @allure.step('判断元素是否可点击')
    def is_click(self, by, locator):
        self.logger.info(f"----------判断元素是否可被点击: {locator}----------")
        try:
            WD(self.driver, self.outTime).until(EC.element_to_be_clickable((self.byDict[by], locator)))
            self.logger.info(f"元素可被点击")
        except TimeoutException:
            self.logger.info(f"元素不可被点击")
            return False
        else:
            return True

    @allure.step('页面跳转到指定frame')
    def switch_to_frame(self, by, locator):
        self.logger.error(f'----------页面开始切换到指定frame：{locator}----------')
        try:
            WD(self.driver, self.outTime).until(EC.frame_to_be_available_and_switch_to_it((self.byDict[by], locator)))
            self.logger.info(f'切换到指定frame成功！')
        except TimeoutException as t:
            self.logger.error(f'切换到指定frame超时！异常为{t}')
            raise t

    @allure.step('切换回默认frame')
    def switch_to_default_frame(self):
        self.logger.info('----------页面开始切换回默认frame----------')
        try:
            self.driver.switch_to.default_content()
            self.logger.info('切换回默认frame成功！')
        except Exception as e:
            self.logger.error(f'切换回默认frame失败!异常为{e}')
            raise e

    @allure.step('判断是否有弹窗,如果有弹窗返回弹窗对象')
    def is_alert(self):
        self.logger.info('----------判断是否有弹窗,如果有弹窗返回弹窗对象----------')
        try:
            alert = WD(self.driver, self.outTime).until(EC.alert_is_present())
            self.logger.info('检测到弹窗，返回弹窗对象alert')
        except (TimeoutException, NoAlertPresentException):
            self.logger.info('未检测到弹窗')
        else:
            return alert

    @allure.step('获取alert弹窗文本')
    def get_alert_text(self):
        self.logger.info('----------获取弹窗对象文本信息----------')
        alert = self.is_alert()
        if alert:
            self.logger.info(f'弹窗对象文本信息为:{alert.text}')
            return alert.text
        else:
            return None


def wait_for_element(self, sel, timeout=20):
    """
    显示等待指定元素的出现。

    @param sel: 定位元素的选择器（可以是 By 选择器、XPath 等）。
    @param timeout: 等待时间，单位为秒，默认为 20 秒。
    @return: 返回等待到的元素。
    """
    return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(sel))


@allure.step('鼠标左键点击')
def ele_click(self, sel, timeout=20):
    """
    执行鼠标左键点击操作。

    @param sel: 定位元素的选择器（可以是 By 选择器、XPath 等）。
    @param timeout: 等待元素可点击的最大时间，单位为秒，默认为 20 秒。
    @return: 如果操作成功，返回 True。
    """
    try:
        element = self.wait_for_element(sel, timeout)
        element.click()
        sleep(0.2)
        selen = re.sub('[^\u4e00-\u9fa5]+', '', str(sel))
        if selen:
            self.logger.info(f"点击：{selen}")
        return True
    except Exception as e:
        self.logger.error(f"无法定位到元素：{sel}，出现异常：\n{e}")
        raise e


@allure.step('输入内容')
def ele_send_key(self, sel, value, timeout=20):
    """
    向指定元素输入内容。

    @param sel: 定位元素的选择器（可以是 By 选择器、XPath 等）。
    @param value: 要输入的内容。
    @param timeout: 等待元素可点击的最大时间，单位为秒，默认为 20 秒。
    @return: 如果操作成功，返回 True。
    """
    try:
        element = self.wait_for_element(sel, timeout)
        element.clear()
        sleep(0.2)
        element.send_keys(value)
        sleep(0.2)
        selen = re.sub('[^\u4e00-\u9fa5]+', '', str(sel))
        if selen:
            self.logger.info(f"点击：{selen}，输入值：{value}")
        return True
    except Exception as e:
        self.logger.error(f"无法定位到元素：{sel}，出现异常：\n{e}")
        raise e


@allure.step('获取指定元素的text值')
def get_ele_text(self, sel, mod=False, timeout=20):
    """
    获取指定元素的文本值。

    @param sel: 定位元素的选择器（可以是 By 选择器、XPath 等）。
    @param mod: 布尔值，决定是否获取 `textContent` 属性值。如果为 True，则返回 `textContent` 的值，否则返回元素的 `text` 属性值。默认为 False。
    @param timeout: 等待元素可点击的最大时间，单位为秒，默认为 20 秒。
    @return: 返回元素的文本值。如果 `mod` 为 True，返回 `textContent` 属性值，否则返回 `text` 属性值。
    """
    try:
        element = self.wait_for_element(sel, timeout)
        text = element.get_attribute('textContent') if mod else element.text
        self.logger.info(f"元素text{':textContent' if mod else ''}: {text}")
        return text
    except Exception as e:
        self.logger.error(f"出现异常：\n{e}")
        raise e


if __name__ == '__main__':
    driver = webdriver.Chrome(service=Service(CHROME_PATH))
    basePage = BasePage(driver)
    basePage.find_element(BT.ID)

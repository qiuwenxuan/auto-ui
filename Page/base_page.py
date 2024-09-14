import re
from time import sleep

import allure
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from common.logger import logger


class BasePage(object):

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('鼠标左键点击')
    def ele_click(self, sel, timeout=20):
        """
        执行鼠标左键点击操作。

        @param sel: 定位元素的选择器（可以是 By 选择器、XPath 等）。
        @param timeout: 等待元素可点击的最大时间，单位为秒，默认为 20 秒。
        @return: 如果操作成功，返回 True。
        """
        try:
            # 显示等待
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(sel)).click()
            sleep(0.2)
            selen = re.sub('[^\u4e00-\u9fa5]+', '', str(sel))
            if len(selen) > 0:
                logger.info(f"点击：【{selen}】")
            return True
        except Exception as e:
            logger.error(f"无法定位到元素：{sel}，出现异常：\n{e}")
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
            # 清除输入框
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(sel)).clear()
            sleep(0.2)
            # 输入内容
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(sel)).send_keys(value)
            sleep(0.2)
            selen = re.sub('[^\u4e00-\u9fa5]+', '', str(sel))
            if len(selen) > 0:
                logger.info(f"点击：【{selen}】，输入值：【{value}】")
            return True
        except Exception as e:
            logger.error(f"无法定位到元素：{sel}，出现异常：\n{e}")
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
            # 显示等待
            element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(sel))
            if not mod:
                logger.info(f"元素text:【{element.text}】")
                return element.text
            else:
                logger.info(f"元素textContent:【{element.get_attribute('textContent')}】")
                return element.get_attribute('textContent')
        except Exception as e:
            logger.error(f"出现异常：\n{e}")
            raise e

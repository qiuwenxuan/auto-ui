from time import sleep
import allure
from typing import List, Union
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as WD
from conftest import logger
from utils.clipBoard import ClipBoard
from utils.keyBoard import KeyBoard


class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver: WebDriver = driver
        self.outTime: int = timeout

        self.byDict = {
            "id": By.ID,
            "name": By.NAME,
            "class_name": By.CLASS_NAME,
            "xpath": By.XPATH,
            "link_text": By.LINK_TEXT,
        }

    def wait_for(self, condition, by=None, locator=None) -> WebElement:
        """
        显示等待通用方法
        @param condition: 期望条件方法,如可见EC.visibility_of_element_located、可点击EC.element_to_be_clickable等
        @param by: 查找元素的方式，例如 By.ID, By.XPATH 等
        @param locator: 要查找的元素的定位值
        @return: WebDriverWait.until() 返回的是等待条件成立时的 WebElement 对象。
        """
        try:
            element = WD(self.driver, self.outTime).until(
                condition((self.byDict[by], locator))
            )
            return element
        except TimeoutException:
            logger.warning(f"元素显示等待超时:{locator}")
            return None

    def find_element(self, by, locator) -> WebElement:
        """页面寻找单个元素"""
        element = self.wait_for(
            EC.visibility_of_element_located, by, locator
        )  # visibility_of_element_located 判断单个元素是否可见
        if element:
            logger.info(f"寻找到元素:{locator}")
            return element
        else:
            logger.warning(f"寻找元素为空:{locator}")
            return None

    def find_elements(self, by, locator) -> List[WebElement]:
        """页面寻找多个元素"""
        element = self.wait_for(
            EC.visibility_of_all_elements_located, by, locator
        )  # visibility_of_all_elements_located 等待指定的多个元素可见
        if element:
            logger.info(f"寻找到多个元素:{locator}")
            return element
        else:
            logger.warning(f"寻找多个元素为空:{locator}")
            return None

    def get_element_text(self, by, locator) -> str:
        """获取元素文本值"""
        element = self.find_element(by, locator)
        if element:
            text = element.text
            logger.info(f"获取到元素文本值: {text}")
            return text
        else:
            logger.warning(f"无法获取元素文本，元素未找到: {locator}")
            return None

    def get_element_attribute(self, by, locator, attr) -> str:
        """
        获取元素属性
        @param attr: 元素属性类型,例如 "class", "href", "id" 等 get_attribute("href")
        """
        element = self.find_element(by, locator)
        if element:
            attribute = element.get_attribute(attr)
            logger.info(f"获取到元素属性值: {attribute}")
            return attribute
        else:
            logger.warning(f"无法获取元素属性值，元素未找到: {locator}")
            return None

    def is_visible(self, by, locator) -> Union[bool, WebElement]:
        """判断元素是否可见"""
        element = self.wait_for(
            EC.visibility_of_element_located, by, locator
        )  # visibility_of_element_located 等待指定元素可见
        if element:
            logger.info(f"元素可见：{locator}")
            return element
        else:
            logger.warning(f"元素不可见：{locator}")
            return False

    def is_click(self, by, locator) -> Union[bool, WebElement]:
        """判断元素是否可被点击"""
        element = self.wait_for(
            EC.element_to_be_clickable, by, locator
        )  # element_to_be_clickable元素可被点击
        if element:
            logger.info(f"元素可被点击:{locator}")
            return element
        else:
            logger.warning(f"等待元素超时，元素不可被点击：{locator}")
            return False

    def is_alert(self) -> Union[bool, WebElement]:
        """判断是否存在弹窗"""
        alert = self.wait_for(EC.alert_is_present())
        if alert:
            logger.info("页面检测到弹窗")
            return alert
        else:
            logger.warning("页面未检测到弹窗")
            return False

    def switch_frame(self, by=None, locator=None):
        """切换frame"""
        if by and locator:
            self.wait_for(EC.frame_to_be_available_and_switch_to_it, by, locator)
            logger.info(f"切换到frame:{locator}")
        else:
            self.driver.switch_to.default_content()
            logger.warning("切换回默认frame")

    def load_url(self, url):
        """打开url"""
        self.driver.get(url)
        logger.info(f"打开url:{url}")

    def clear(self, by, locator):
        """清空输入框"""
        element = self.find_element(by, locator)
        if element:
            element.clear()
            logger.info(f"清空输入框：{locator}")
        else:
            logger.warning(f"未找到需要清空的输入框：{locator}")

    def send_keys(self, by, locator, value=""):
        """输入文本内容"""
        element = self.find_element(by, locator)
        if element:
            element.send_keys(value)
            logger.info(f"输入框输入内容：{locator} 输入：{value}")
        else:
            logger.warning(f"输入框输入内容失败：{locator}")

    def click(self, by, locator):
        """点击事件"""
        element = self.wait_for(
            EC.element_to_be_clickable, by, locator
        )  # element_to_be_clickable元素可被点击
        if element:
            element.click()
            logger.info(f"点击元素:{locator}")
        else:
            logger.warning(f"元素点击失败：{locator}")

    def sleep(self, num=0):
        """强制等待"""
        logger.info(f"页面强制等待{num}s")
        sleep(num)

    def select_checkbox(self, by, locator):
        """选择复选框"""
        checkbox = self.find_element(by, locator)
        if not checkbox.is_selected():
            self.click(by, locator)
        logger.info(f"选择复选框：{locator}")

    def deselect_checkbox(self, by, locator):
        """取消复选框"""
        checkbox = self.find_element(by, locator)
        if checkbox.is_selected():
            self.click(by, locator)
            logger.info(f"取消复选框：{locator}")

    def ctrl_v(self, value):
        """ctrl+v 粘贴自定义文本"""
        ClipBoard.set_text(value)
        self.sleep(3)
        KeyBoard.two_keys("ctrl", "v")
        logger.info(f"键盘输入ctrl+v粘贴文本：{value}")

    def enter_key(self):
        """鼠标点击enter回车"""
        KeyBoard.one_key("enter")
        logger.info(f"鼠标点击enter回车")


if __name__ == "__main__":
    pass

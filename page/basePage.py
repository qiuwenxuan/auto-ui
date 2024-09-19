from time import sleep

import allure
from selenium.common import TimeoutException, NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as WD

from common.logger import LoggerManager
from utils.clipboard import ClipBoard
from utils.keyboard import KeyBoard


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
        try:
            self.logger.info(f'----------页面寻找单个元素：【{locator}】----------')
            element = WD(self.driver, self.outTime).until(lambda x: x.find_element(self.byDict[by], locator))
            self.logger.info(f'元素【{locator}】被找到')
        except TimeoutException:
            self.logger.error(f'寻找元素【{locator}】超时，元素未被找到')
            return None
        else:
            return element

    @allure.step('页面寻找多个元素')
    def find_elements(self, by, locator):
        try:
            self.logger.info(f'----------页面寻找多个元素：【{locator}】----------')
            element = WD(self.driver, self.outTime).until(lambda x: x.find_elements(self.byDict[by], locator))
            self.logger.info(f'多个元素【{locator}】被找到')
        except TimeoutException:
            self.logger.error(f'寻找多个元素【{locator}】超时,元素未找到')
            return None
        else:
            return element

    @allure.step('获取alert弹窗文本')
    def get_alert_text(self):
        alert = self.is_alert()
        self.logger.info('----------获取弹窗对象文本信息----------')
        if alert:
            self.logger.info(f'弹窗对象文本信息为:{alert.text}')
            return alert.text
        else:
            self.logger.error('未获取到弹窗的文本信息')
            return None

    @allure.step('获取目标元素的文本信息')
    def get_element_text(self, by, locator, name=None):
        # name是获取元素的属性，例如 "class", "href", "id" 等。get_attribute("href")
        self.logger.info(f'----------获取目标元素属性：【{locator}】----------')
        element = self.find_element(by, locator)
        if element and name:
            # name属性不为null，表示获取元素属性信息
            value = element.get_attribute(name)
            self.logger.info(f'获取元素{name}属性，值为{value}')
            return value
        elif element and not name:
            text = element.text
            self.logger.info(f'获取元素text文本信息，值为{text}')
            return text
        else:
            self.logger.error(f'目标元素属性未获取到')
            return None

    @allure.step('判断元素是否可见')
    def is_element_visible(self, by, locator):
        self.logger.info(f'----------判断元素是否可见：【{locator}】----------')
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
        self.logger.info(f"----------判断元素是否可被点击: 【{locator}】----------")
        try:
            element = WD(self.driver, self.outTime).until(EC.element_to_be_clickable((self.byDict[by], locator)))
            self.logger.info(f"元素可被点击")
        except TimeoutException:
            self.logger.info(f"元素不可被点击")
            return False
        else:
            return element

    @allure.step('判断是否有弹窗,如果有则返回弹窗对象')
    def is_alert(self):
        self.logger.info('----------判断页面是否有弹窗----------')
        try:
            alert = WD(self.driver, self.outTime).until(EC.alert_is_present())
            self.logger.info('检测到弹窗')
        except (TimeoutException, NoAlertPresentException):
            self.logger.error('未检测到弹窗')
            return None
        else:
            return alert

    @allure.step('页面切换frame')
    def switch_frame(self, by=None, locator=None):
        self.logger.info(f'----------页面切换frame【{locator}】----------')
        if by and locator:
            self.logger.info(f'切换到frame: 【{locator}】')
            WD(self.driver, self.outTime).until(EC.frame_to_be_available_and_switch_to_it((self.byDict[by], locator)))
        else:
            self.logger.info('切换回默认frame')
            WD(self.driver, self.outTime).until(self.driver.switch_to.default_content())

    @allure.step('对输入框输入文本内容')
    def send_keys(self, by, locator, value=''):
        self.logger.info(f'----------对输入框【{locator}】输入文本内容：{value}----------')
        element = self.find_element(by, locator)
        if element:
            self.clear(by, locator)
            element.send_keys(value)
            self.logger.info(f'对指定输入框输入内容：{value}')
        else:
            self.logger.error(f'输入框元素未找到')

    @allure.step('清空输入框')
    def clear(self, by, locator):
        element = self.find_element(by, locator)
        element.clear()
        self.logger.info(f'----------清空输入框：【{locator}】----------')

    @allure.step('点击目标元素')
    def click(self, by, locator):
        element = self.is_click(by, locator)
        if element:
            element.click()
        self.logger.info(f'----------点击目标元素:【{locator}】----------')

    @allure.step('页面强制等待')
    def sleep(self, num=0):
        self.logger.info(f'----------页面强制等待{num}s----------')
        sleep(num)

    @allure.step('鼠标点击ctrl+v粘贴')
    def ctrl_v(self, value):
        ClipBoard.set_text(value)
        self.sleep(3)
        KeyBoard.two_keys('ctrl', 'v')
        self.logger.info(f'----------键盘输入ctrl+v粘贴文本：{value}----------')

    @allure.step('鼠标点击enter回车')
    def enter_key(self):
        KeyBoard.one_key('enter')
        self.logger.info(f'----------鼠标点击enter回车----------')


if __name__ == '__main__':
    pass

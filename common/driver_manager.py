from enum import Enum
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from common.logger import logger
from data.constant import Const


class BrowserType(Enum):
    CHROME = "chrome"
    EDGE = "edge"


# 设置别名 BT
BT = BrowserType


class DriverManager:
    """负责 WebDriver 的创建和销毁"""

    def __init__(self, browser_type: BT, wait_time: int = 10):
        """
        初始化 DriverManager，根据浏览器类型创建对应的 WebDriver 实例
        @param browser_type: 浏览器类型 (BT.CHROME 或 BT.EDGE)
        @param wait_time: 隐式等待时间，默认10秒
        """
        self.driver = self._create_driver(browser_type, wait_time)

    def _create_driver(self, browser_type: BT, wait_time: int):
        """
        根据传入的浏览器类型创建 WebDriver 实例
        @param browser_type: 浏览器类型 (BT 枚举)
        @param wait_time: 隐式等待时间
        @return: WebDriver对象
        """
        driver: webdriver = None
        if browser_type == BT.CHROME:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--incognito")
            driver = webdriver.Chrome(service=Service(Const.CHROME_PATH), options=chrome_options)
        elif browser_type == BT.EDGE:
            edge_options = webdriver.EdgeOptions()
            edge_options.add_argument("--incognito")
            driver = webdriver.Edge(service=Service(Const.EDGE_PATH), options=edge_options)
        else:
            raise ValueError("Unsupported browser type. Please use BT.CHROME or BT.EDGE.")

        logger.info(f"启动 {browser_type.value} 浏览器")
        driver.maximize_window()
        logger.info("最大化浏览器窗口")
        driver.implicitly_wait(wait_time)
        logger.info(f"设置隐式等待时间为 {wait_time}s")
        return driver


# 设置默认为chromeDriver单例
chromeManager = DriverManager(BT.CHROME)
edgeManager = DriverManager(BT.EDGE)

if __name__ == '__main__':
    driver = DriverManager(BT.CHROME).driver
    logger.info(driver)
    sleep(2)
    driver.quit()

    driver = DriverManager(BT.EDGE).driver
    logger.info(driver)
    sleep(2)
    driver.quit()

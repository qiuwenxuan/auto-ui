import pytest
from selenium import webdriver

from common.logger import LoggerManager


# 定义全局变量logger
logger = LoggerManager().get_logger()


# 设置级别为scope="session"，表示全部用例只执行一次
@pytest.fixture(scope="session")
def driver():
    logger.info("------------打开浏览器------------")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    logger.info("------------关闭浏览器------------")
    driver.quit()

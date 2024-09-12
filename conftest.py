import pytest
from selenium import webdriver

from common.logger import setup_logger
from settings import ENV

# 定义全局常量
logger = setup_logger()
wait_time = 20


@pytest.fixture(scope="class")
def login():
    """初始化Chrome浏览器驱动"""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")  # 启用隐私模式
    driver = webdriver.Chrome(options=chrome_options)
    logger.info(f"启用隐私模式加载浏览器驱动")
    # 登录网易163浏览器
    driver.maximize_window()
    logger.info("打开浏览器界面")
    driver.get(ENV.url)
    logger.info(f"打开网址 url:{ENV.url}")

    driver.implicitly_wait(wait_time)
    logger.info(f"设置隐式等待时间为{wait_time}s")
    yield driver
    driver.quit()
    logger.info("关闭浏览器")

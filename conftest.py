import time

import pytest
from selenium import webdriver

from common.logger import logger
from data.config import LOGIN_URL, SQL_DELETE, SQL_INSERT


def login():
    """初始化Chrome浏览器驱动并登录到网站"""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")  # 启用隐私模式
    driver = webdriver.Chrome(options=chrome_options)
    logger.info(f"启用隐私模式加载浏览器驱动")
    # 初始化测试数据
    from common.sql_manager import sm
    sm.execute(SQL_DELETE)
    sm.execute(SQL_INSERT)
    logger.info(f"初始化测试数据")
    # 打开浏览器网址
    driver.maximize_window()
    logger.info("打开浏览器界面")
    driver.get(LOGIN_URL)
    logger.info(f"打开网址 url:{LOGIN_URL}")
    # 设置等待时间
    driver.implicitly_wait(20)
    logger.info(f"设置隐式等待时间为{20}s")
    yield driver
    # 关闭浏览器
    driver.quit()
    logger.info("关闭浏览器")


# 测试用例计时器
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
# tryfirst=True 如果有多个 pytest_runtest_setup 钩子，这个钩子会优先执行;
# hookwrapper=True 让这个钩子变成一个包装器，能够在 pytest 执行钩子链前后插入逻辑
def pytest_runtest_setup(item):
    """在每个测试用例运行前调用，用于记录测试开始时间"""
    item.start_time = time.time()  # 记录测试用例开始时间
    yield  # 将控制权交回给 pytest，执行其他相关的 setup 钩子
    # pytest 执行完所有相关 setup 操作后，继续执行此处的代码
    logger.info(f"开始执行测试用例: {item.name}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_teardown(item):
    """在每个测试用例结束后调用，用于计算和记录测试耗时"""
    yield
    end_time = time.time()  # 记录测试用例结束时间
    duration = end_time - item.start_time  # 计算测试用例执行时间
    logger.info(
        f"测试用例 '{item.name}' 执行耗时: {duration:.4f} s")


# 初始化清理测试数据
def pytest_sessionstart(session):
    """
    在测试会话开始时初始化测试数据。
    @param session: pytest的session对象
    """
    logger.info("测试会话开始，初始化测试数据")
    # 执行 SQL 初始化脚本
    try:
        from common.sql_manager import sm
        sm.execute(SQL_DELETE)
        sm.execute(SQL_INSERT)
        logger.info("测试数据初始化完成")
    except Exception as e:
        logger.error(f"初始化测试数据时发生错误: {e}")
        raise e


def pytest_sessionfinish(session, exitstatus):
    """
    在测试会话结束时进行必要的清理操作。
    @param session: pytest的session对象
    @param exitstatus: 测试执行状态码
    """
    logger.info("测试会话结束，清理测试数据")
    try:
        from common.sql_manager import sm
        sm.execute(SQL_DELETE)
        sm.execute(SQL_INSERT)
        logger.info("测试数据清理完成")
    except Exception as e:
        logger.error(f"清理测试数据时发生错误: {e}")
        raise e

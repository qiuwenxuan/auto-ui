from datetime import datetime
from selenium.webdriver.chrome.service import Service
import os
import allure
from time import time
import pytest
from selenium import webdriver
from common.logger import LoggerManager
from config.conf import CHROME_PATH, IMAGE_DIR


# 定义全局变量
_driver = None
logger = LoggerManager().get_logger()


# 设置级别为scope="session"，表示全部用例只执行一次
@pytest.fixture(scope="session")
def driver():
    """创建全局唯一一个driver"""
    logger.info("============打开浏览器============")
    global _driver
    _driver = webdriver.Chrome(service=Service(CHROME_PATH))
    _driver.maximize_window()
    _driver.implicitly_wait(10)
    yield _driver
    logger.info("============关闭浏览器============")
    _driver.quit()


# 测试失败时保存截图到指定路径
# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#     当测试失败时，自动截图并保存到指定路径
#     """
#     outcome = yield
#     report = outcome.get_result()


#     if report.when == "call" or report.when == "setup":
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             test_name = report.nodeid.replace("::", "_")
#             timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#             screenshot_path = f"{SCREENSHOT_DIR}/{test_name}_{timestamp}.png"
#             _driver.save_screenshot(screenshot_path)  # 保存截图
#             logger.info(f"测试失败，截图已保存到: {screenshot_path}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """获取每个用例状态的钩子函数"""
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()

    # rep.when可选参数有call、setup、teardown，
    # call表示为用例执行环节、setup、teardown为环境初始化和清理环节
    # rep.when == "call"表示这里只针对用例执行且失败的用例进行异常截图
    if rep.when == "call" and rep.failed and not hasattr(rep, "wasxfail"):
        # 拼接错误截图url路径
        test_name = (
            rep.nodeid.split("/")[-1]
            .replace(".py", "")
            .replace("::", " ")
            .replace("[", " ")
            .replace("]", "")
        )
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = f"{IMAGE_DIR}\{test_name}_{timestamp}.png"
        logger.info(
            f"test_name:{test_name},timestamp:{timestamp},screenshot_path:{screenshot_path}"
        )
        _driver.save_screenshot(screenshot_path)
        logger.info(f"测试失败，截图已保存到: {screenshot_path}")

        # 添加截图到 Allure 报告
        screenshot_png = _driver.get_screenshot_as_png()
        with allure.step("添加失败截图..."):
            allure.attach(screenshot_png, "失败截图", allure.attachment_type.PNG)


@pytest.fixture(autouse=True)
def record_time():
    """计时fixture,autouse=True表示所有测试用例都会自动使用这个fixture进行计时"""
    logger.info("------------开始执行测试用例------------")
    start_time = time()  # 记录开始时间
    # 测试用例的执行部分
    yield
    # 测试用例执行完毕后，计算执行时间
    end_time = time()
    duration = end_time - start_time
    logger.info(f"------------测试用例执行结束，耗时{duration:.4f}秒------------")

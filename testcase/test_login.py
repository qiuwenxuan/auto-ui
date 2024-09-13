import pytest
from selenium.webdriver.common.by import By

from operation.selenium_co import ele_click, ele_send_key, get_ele_text
from conftest import open_page, logger


@pytest.mark.parametrize('username,password,result', [('qwx13057573527', 'qwx#125617', 'qwx13057573527'),
                                                      ('qwx', 'qwx#125617', '用户名错误'),
                                                      ('qwx13057573527', 'qwx', '密码错误')],
                         ids=('test_login_001', 'test_login_002', 'test_login_003'))
def test_login(username, password, result, open_page):
    # 获取驱动
    driver = open_page

    # 输入账户和密码
    ele_send_key(driver, (By.XPATH, '//*[@placeholder="请输入用户名"]'), username)
    ele_send_key(driver, (By.XPATH, '//*[@placeholder="请输入密码"]'), password)
    logger.info(f"输入账户和密码username:【{username}】 password:【{password}】")

    # 点击登录
    ele_click(driver, (By.XPATH, '//input[@value="登录"]'))

    if result == 'qwx13057573527':
        # 断言测试结果
        text = get_ele_text(driver, (By.XPATH, '//*[@class="login_btn fl"]/em[1]'))
        logger.info(f"assert值：【{text}】")
        assert text == result
        ele_click(driver, (By.XPATH, '//a[@href|text()="退出"]'))
        ele_click(driver, (By.XPATH, '//a[@href|text()="登录"]'))
    elif result == "用户名错误":
        # 获取"账号或密码错误"的字眼
        text = get_ele_text(driver, (By.XPATH, '//*[@class="user_error"]'))
        logger.info(f"assert值：【{text}】")
        assert text == result
    elif result == "密码错误":
        # 获取"账号或密码错误"的字眼
        text = get_ele_text(driver, (By.XPATH, '//*[@class="pwd_error"]'))
        logger.info(f"assert值：【{text}】")
        assert text == result

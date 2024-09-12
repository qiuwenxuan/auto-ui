import pytest
from selenium.webdriver.common.by import By

from common.selenium_co import ele_click, ele_send_key, get_ele_text
from common.utils import xpath_tuple
from conftest import login, logger


@pytest.mark.parametrize('username,password,result', [('qwx13057573527', 'qwx#125617', 'qwx13057573527'),
                                                      ('qwx', 'qwx#125617', '用户名错误'),
                                                      ('qwx13057573527', 'qwx', '密码错误')],
                         ids=('test_shopping_mail_001', 'test_shopping_mail_002', 'test_shopping_mail_003'))
def test_register(username, password, result, login):
    # 获取驱动
    driver = login
    # 点击立即注册
    ele_click(driver, xpath_tuple('//a[@href|text()="立即注册"]'))
    # 输入账户和密码
    ele_send_key(driver, xpath_tuple('//label[contains(text(),"用户名")]'), username)

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

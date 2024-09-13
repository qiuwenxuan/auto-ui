import pytest
from selenium.webdriver.common.by import By

from common.logger import logger
from operation.selenium_co import ele_click, ele_send_key, get_ele_text
from common.utils import xpath_tuple
from conftest import open_page
from po.event import Event


@pytest.mark.parametrize('username,password,email', [('wenxuan1', 'qwx#125617', '1737739958@qq.com'),
                                                     ('wenxuan2', 'qwx#125617', '1737739928@qq.com'),
                                                     ('wenxuan3', 'qwx#125617', '1737739sd8@qq.com')],
                         ids=('test_register_001', 'test_register_002', 'test_register_003'))
def test_register(username, password, email, open_page):
    # 获取驱动
    driver = open_page
    # 点击立即注册
    ele_click(driver, xpath_tuple('//a[@href|text()="立即注册"]'))
    # 输入注册信息
    ele_send_key(driver, xpath_tuple('//label[contains(text(),"用户名")]/following-sibling::*[1]'), username)
    ele_send_key(driver, xpath_tuple('//label[contains(text(),"密码")]/following-sibling::*[1]'), password)
    ele_send_key(driver, xpath_tuple('//label[contains(text(),"确认密码")]/following-sibling::*[1]'), password)
    ele_send_key(driver, xpath_tuple('//label[contains(text(),"邮箱")]/following-sibling::*[1]'), email)
    # 点击注册按钮
    ele_click(driver, xpath_tuple('//*[@class="reg_sub"]/*[@value="注 册"]'))

    # 断言1：判断数据库表df_user_userinfo内是否存在username
    from common.sql_manager import sqlObject
    result = sqlObject.execute([f"SELECT uname FROM df_user_userinfo WHERE uname='{username}'"])
    logger.info(f"assert值：【{result}】")
    assert username in str(result)

    # 断言2：判断注册的账号是否能够登录成功
    # 输入账户和密码
    Event().login(driver, username, password)
    # 断言测试结果
    text = get_ele_text(driver, (By.XPATH, '//*[@class="login_btn fl"]/em[1]'))
    logger.info(f"assert值：【{text}】")
    assert text == username
    ele_click(driver, xpath_tuple('//a[@href|text()="退出"]'))
    ele_click(driver, xpath_tuple('//a[@href|text()="登录"]'))

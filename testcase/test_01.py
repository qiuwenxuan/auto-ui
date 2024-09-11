from time import sleep

import pytest
from selenium.webdriver.common.by import By

from conftest import login, logger


@pytest.mark.parametrize('username,password,result', [('qwx13057573527', 'qwx#125617', 'qwx13057573527@163.com'),
                                                      ('qwx', 'qwx#125617', '账号或密码错误'),
                                                      ('qwx13057573527', 'qwx', '账号或密码错误')],
                         ids=('test_shopping_mail_001', 'test_shopping_mail_002', 'test_shopping_mail_003'))
def test_login_mail(username, password, result, login):
    # 获取login fixture返回的driver驱动
    driver = login

    # 转换到登录的iframe内
    driver.switch_to.frame(
        driver.find_element(By.XPATH, '//*[@id="loginDiv"]/iframe'))  # frame_reference为frame标签的特征

    # 输入账户和密码
    driver.find_element(By.XPATH, '//*[@placeholder="邮箱账号或手机号码"]').clear()
    driver.find_element(By.XPATH, '//*[@placeholder="邮箱账号或手机号码"]').send_keys(username)

    driver.find_element(By.XPATH, '//*[@placeholder="输入密码"]').clear()
    driver.find_element(By.XPATH, '//*[@placeholder="输入密码"]').send_keys(password)
    logger.info(f"输入账户和密码username:{username}\npassword:{password}")

    # 点击登录确定
    driver.find_element(By.XPATH, '//*[@id="dologin"]').click()
    logger.info(f"点击登录按钮")
    sleep(1)
    if result in 'qwx13057573527@163.com':
        # 切换到主body
        driver.switch_to.default_content()
        # 断言测试结果
        text = driver.find_element(By.XPATH, '//*[@id="spnUid"]').text
        logger.info("断言账户名称user:" + text)
        assert text == result
    else:
        # 获取"账号或密码错误"的字眼
        text = driver.find_element(By.XPATH, '//*[@class="ferrorhead"]').text
        logger.info("断言警告信息：" + text)
        assert text == result

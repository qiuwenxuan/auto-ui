import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin:

    def setup_class(self):
        """初始化Chrome浏览器驱动"""

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")  # 启用隐私模式
        self.driver = webdriver.Chrome(options=chrome_options)

        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def teardown_class(self):
        """关闭浏览器驱动"""
        self.driver.quit()

    @pytest.mark.parametrize('username,password,result', [('qwx13057573527', 'qwx#125617', 'qwx13057573527@163.com'),
                                                          ('qwx', 'qwx#125617', '账号或密码错误'),
                                                          ('qwx13057573527', 'qwx', '账号或密码错误')],
                             ids=('test_shopping_mail_001', 'test_shopping_mail_002', 'test_shopping_mail_003'))
    def test_login_mail(self, username, password, result):
        # 登录网易163浏览器
        self.driver.get('https://mail.163.com/')
        # 转换到登录的iframe内
        self.driver.switch_to.frame(
            self.driver.find_element(By.XPATH, '//*[@id="loginDiv"]/iframe'))  # frame_reference为frame标签的特征
        # 输入账户
        self.driver.find_element(By.XPATH, '//*[@placeholder="邮箱账号或手机号码"]').clear()
        self.driver.find_element(By.XPATH, '//*[@placeholder="邮箱账号或手机号码"]').send_keys(username)
        # 输入密码
        self.driver.find_element(By.XPATH, '//*[@placeholder="输入密码"]').clear()
        self.driver.find_element(By.XPATH, '//*[@placeholder="输入密码"]').send_keys(password)
        # 点击登录确定
        self.driver.find_element(By.XPATH, '//*[@id="dologin"]').click()
        if result in 'qwx13057573527@163.com':
            # 切换到主body
            self.driver.switch_to.default_content()
            # 断言测试结果
            text = self.driver.find_element(By.XPATH, '//*[@id="spnUid"]').text
            assert text == result
            # 退出当前账号
            self.driver.find_element(By.XPATH, '//*[@id="spnUid"]').click()
            self.driver.find_element(By.XPATH, '//*[text()="退出登录"]').click()
        else:
            # 获取"账号或密码错误"的字眼
            text = self.driver.find_element(By.XPATH, '//*[@class="ferrorhead"]').text
            assert text == result

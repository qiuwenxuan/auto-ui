from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from data.constant import CHROME_PATH, EDGE_PATH


class DriverManager:
    """负责 WebDriver 的创建和销毁"""

    @staticmethod
    def get_chromedriver():
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        # 创建 Service 对象，指定驱动程序的路径
        s = Service(CHROME_PATH)

        # 使用 Service 对象创建 WebDriver 实例
        driver = webdriver.Chrome(service=s, options=chrome_options)
        driver.implicitly_wait(10)
        return driver

    @staticmethod
    def get_edgedriver():
        edge_options = webdriver.EdgeOptions()
        edge_options.add_argument("--incognito")
        # 创建 Service 对象，指定驱动程序的路径
        s = Service(EDGE_PATH)

        # 使用 Service 对象创建 WebDriver 实例
        driver = webdriver.Edge(service=s, options=edge_options)
        driver.implicitly_wait(10)
        return driver

    @staticmethod
    def quit_driver(driver):
        driver.quit()


if __name__ == '__main__':
    edgedriver = DriverManager.get_edgedriver()
    print(edgedriver)
    DriverManager.quit_driver(edgedriver)

    chromedriver = DriverManager.get_chromedriver()
    print(chromedriver)
    DriverManager.quit_driver(chromedriver)


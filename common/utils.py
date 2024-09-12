from selenium.webdriver.common.by import By


def xpath_tuple(xpath_str: str) -> tuple:
    return By.XPATH, xpath_str


if __name__ == '__main__':
    xpath = xpath_tuple('//a[@href|text()="立即注册"]')
    print(xpath)
    print(type(xpath))

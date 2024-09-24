import os
from datetime import datetime

"""global path"""
# 当前时间
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# 当前日期
DATE_TIME = datetime.now().strftime("%Y-%m-%d")

# 项目根目录
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 屏幕截图存放目录
SCREENSHOT_DIR = os.path.join(ROOT_DIR, "report", "image")
# 测试报告目录
REPORT_DIR = os.path.join(ROOT_DIR, "report", "TestReport")
# 测试数据目录
DATA_DIR = os.path.join(ROOT_DIR, "data")

# 当前脚本路径
CURRENT_PATH = os.path.abspath(__file__)
# 配置文件路径
CONF_PATH = os.path.join(ROOT_DIR, "config", "config.ini")
# 日志文件输出路径
LOG_PATH = os.path.join(ROOT_DIR, "report", "log", "app.log")
# 数据库文件路径
SQL_FILE = os.path.join(ROOT_DIR, "db.sqlite3")
# chrome driver路径
CHROME_PATH = os.path.join(ROOT_DIR, "driver", "chromedriver.exe")
# edge driver路径
EDGE_PATH = os.path.join(ROOT_DIR, "driver", "msedgedriver.exe")


if __name__ == "__main__":
    print("CURRENT_TIME:{}".format(CURRENT_TIME))
    print("DATE_TIME:{}".format(DATE_TIME))
    print("ROOT_DIR:{}".format(ROOT_DIR))
    print("SCREENSHOT_DIR:{}".format(SCREENSHOT_DIR))
    print("REPORT_DIR:{}".format(REPORT_DIR))
    print("DATA_DIR:{}".format(DATA_DIR))
    print("CURRENT_PATH:{}".format(CURRENT_PATH))
    print("CONF_PATH:{}".format(CONF_PATH))
    print("LOG_DIR:{}".format(LOG_PATH))
    print("SQL_FILE:{}".format(SQL_FILE))
    print("CHROME_PATH:{}".format(CHROME_PATH))
    print("EDGE_PATH:{}".format(EDGE_PATH))

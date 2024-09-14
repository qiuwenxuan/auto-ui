import os
from datetime import datetime


class Const:
    """global path"""
    # 工作目录
    WORKSPACE_DIR = os.getcwd()
    # 当前脚本路径
    CURRENT_PATH = os.path.abspath(__file__)
    # 项目根目录
    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 测试报告目录
    REPORT_DIR = os.path.join(ROOT_DIR, 'report')
    # 日志配置文件所在目录
    LOG_INPUT_DIR = os.path.join(ROOT_DIR, 'logs')
    # 输出日志文件目录
    LOG_PATH = os.path.join(ROOT_DIR, 'data', 'config', 'logger.yaml')
    # 配置文件路径
    CONF_PATH = os.path.join(ROOT_DIR, 'data', 'config', 'config.yaml')
    # 测试数据所在目录
    DATA_PATH = os.path.join(ROOT_DIR, 'data', 'tcData.xlsx')
    # 当前时间
    CURRENT_TIME = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # chrome driver路径
    CHROME_PATH = os.path.join(ROOT_DIR, 'driver', 'chromedriver.exe')
    # edge driver路径
    EDGE_PATH = os.path.join(ROOT_DIR, 'driver', 'msedgedriver.exe')


if __name__ == '__main__':
    print("工作目录:" + Const.WORKSPACE_DIR)
    print("当前脚本路径:" + Const.CURRENT_PATH)
    print("项目根目录:" + Const.ROOT_DIR)
    print("测试报告目录:" + Const.REPORT_DIR)
    print("配置文件所在目录:" + Const.LOG_PATH)
    print("输出日志文件目录:" + Const.LOG_INPUT_DIR)
    print("测试数据所在目录:" + Const.DATA_PATH)
    print("当前时间:" + Const.CURRENT_TIME)
    print("CHROME_PATH:" + Const.CHROME_PATH)
    print("EDGE_PATH:" + Const.EDGE_PATH)

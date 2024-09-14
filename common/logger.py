import logging
import logging.config
import os

import yaml

from data.constant import Const


class LoggerManager:
    def __init__(self, default_path: str = Const.LOG_PATH, default_output: str = Const.LOG_INPUT_DIR,
                 default_level: int = logging.INFO):
        """
        初始化 Logger 对象，尝试从配置文件中加载日志配置。

        @param default_path: 日志配置文件路径。
        @param default_output: 日志文件输出目录。
        @param default_level: 默认日志级别，默认为 logging.INFO。
        """
        self.default_path = default_path
        self.default_output = default_output
        self.default_level = default_level

        # 配置日志记录器
        if os.path.exists(self.default_path):
            try:
                with open(self.default_path, 'rt', encoding='utf-8') as file:
                    config = yaml.safe_load(file.read())

                    # 确保日志文件输出路径存在
                    if 'handlers' in config and 'file_handler' in config['handlers']:
                        config['handlers']['file_handler']['filename'] = os.path.join(self.default_output, 'info.log')

                    logging.config.dictConfig(config)
                    logging.getLogger("logger").info("Logger日志对象初始化成功！")
            except Exception as e:
                # 捕获配置文件加载中的异常
                logging.basicConfig(level=self.default_level)
                logging.error(f"日志配置文件加载失败，使用默认日志配置。错误信息: {e}")
        else:
            logging.basicConfig(level=self.default_level)
            logging.warning(f"警告: 找不到日志配置文件 {self.default_path}。使用默认日志配置。")

    def get_logger(self, name: str = "logger") -> logging.Logger:
        """
        获取 logger 对象。

        @param name: logger 名称，默认为 "logger"。
        @return: 配置后的 logger 对象。
        """
        return logging.getLogger(name)


# 单例模式
logger = LoggerManager().get_logger()
if __name__ == '__main__':
    logger = LoggerManager().get_logger()
    logger.error(logger)
    logger.info("hello world!")

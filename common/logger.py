import logging
import os

from config.conf import LOG_PATH


class LoggerManager:
    def __init__(self, log_file: str = LOG_PATH, log_level: int = logging.INFO):
        """
        @param log_file: str 日志文件的路径
        @param log_level: int 日志记录级别
        """
        self.logger = logging.getLogger('logger')
        self.logger.setLevel(log_level)
        self.setup_logger(log_file)

    def setup_logger(self, log_file: str):
        """
        配置日志文件的handler和编码为utf-8
        @param log_file: str 日志文件的路径
        """
        if not self.logger.handlers:  # 防止重复添加handler
            # 确保日志文件的目录存在
            log_dir = os.path.dirname(log_file)
            if log_dir and not os.path.exists(log_dir):
                os.makedirs(log_dir)

            # 创建FileHandler
            file_handler = logging.FileHandler(log_file, encoding='utf-8')
            file_handler.setLevel(logging.INFO)
            file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

            # 添加handler到logger
            self.logger.addHandler(file_handler)

            # 创建FileHandler
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)
            console_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

            # 添加handler到logger
            self.logger.addHandler(console_handler)

    # 确保logger自定义对象为单例且唯一
    def get_logger(self) -> logging.Logger:
        """
        返回logger对象
        @return logging.Logger 已配置好的logger实例
        """
        return self.logger


if __name__ == '__main__':
    logger = LoggerManager().get_logger()
    logger.debug("this is a debug log...")
    logger.info("this is a info log...")
    logger.warning("this is a warning log...")
    logger.critical("this is a critical log...")

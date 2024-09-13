import logging.config
import os

import yaml


def setup_logger(default_path=LOG_PATH, default_output=LOG_INPUT_DIR, default_level=logging.INFO):
    r"""
    根据logger配置文件初始化自定义logger
    @param default_path: 默认的日志配置文件路径。 C:\Users\v-williamqiu\Desktop\wx\workspace\auto-ui\config\logger.yaml
    @param default_output: 默认日志输出路径 C:\Users\v-williamqiu\Desktop\wx\workspace\auto-ui\logs
    @param default_level: 如果没有提供配置文件，使用的默认日志级别。
    @return:
    """

    # 尝试从配置文件中加载日志配置
    if os.path.exists(default_path):
        with open(default_path, 'rt', encoding='utf-8') as file:
            config = yaml.safe_load(file.read())
            # 设置日志文件info.log输出路径
            config['handlers']['file_handler']['filename'] = os.path.join(default_output, 'info.log')
            logging.config.dictConfig(config)
            logger = logging.getLogger("logger")
            logger.info("Logger日志对象初始化成功！")
            return logger
    else:
        logging.basicConfig(level=default_level)
        logging.info(f"警告: 找不到日志配置文件 {default_path}。使用默认logging日志对象。")
        return logging


# 实例化日志器
logger = setup_logger()

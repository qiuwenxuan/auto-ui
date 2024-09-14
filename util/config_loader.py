import os

import yaml

from data.constant import Const


class ConfigLoader:
    def __init__(self, config_file=Const.CONF_PATH):
        """
        初始化配置加载器，加载yaml配置文件

        @param config_file: str 配置文件路径
        """
        self.config_file = config_file
        self.config = self._load_config()

    def _load_config(self):
        """
        私有方法，加载yaml配置文件

        @return: dict 加载的配置数据
        """
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"配置文件 {self.config_file} 不存在")

        with open(self.config_file, 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)
            return config

    def get_value(self, *keys):
        """
        获取指定的配置项值，支持通过多级键来获取嵌套配置

        @param keys: tuple 传入层级的键
        @return: 返回指定配置项的值
        """
        data = self.config
        for key in keys:
            data = data.get(key)
            if data is None:
                raise KeyError(f"配置项 {'.'.join(keys)} 不存在")
        return data


confloader = ConfigLoader()
# 使用示例
if __name__ == "__main__":
    # 假设yaml文件路径是config.yaml
    config_loader = ConfigLoader(Const.CONF_PATH)

    # 获取单个配置变量：例如获取用户名
    username = config_loader.get_value("env", "username")
    print("用户名:", username)

    # 获取单个配置变量：例如获取SQL文件路径
    sql_file = config_loader.get_value("sql", "sql_file")
    print("SQL文件路径:", sql_file)

# 项目名称：Auto-UI

## 项目结构

```plaintext
auto-ui/
│
├── testcase/                 # 测试用例目录
│
├── pages/                    # 页面对象模式 (POM) 的页面类
│
├── config/                   # 配置文件目录
│
├── data/                     # 测试数据目录
│
├── utils/                    # 公共方法和工具函数
│
├── common/                   # 公共类目录
│
├── reports/                  # 测试报告目录
│   ├── image/                # 图片目录
│   ├── log/                  # 日志生成目录
│   └── TestReport/           # 测试报告文件目录
│
├── drivers/                  # 浏览器驱动目录
│   ├── msedgedriver.exe      # Edge浏览器驱动
│   └── chromedriver.exe      # Chrome浏览器驱动
│
├── conftest.py               # pytest全局配置和钩子
├── pytest.ini                # pytest配置文件
├── requirements.txt          # 项目依赖的包列表
├── db.sqlite3                # SQLite3数据库文件
├── .gitignore                # Git忽略文件
└── README.md                 # 项目说明文件

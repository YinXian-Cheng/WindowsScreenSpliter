import configparser
import os

# 读取配置文件
config = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
config.read(config_path)

# 获取APP1和APP2的配置信息
app1_title = config['APP1']['title']
app1_path = config['APP1']['path']
app2_title = config['APP2']['title']
app2_path = config['APP2']['path']

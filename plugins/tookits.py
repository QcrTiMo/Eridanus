import logging

import colorlog
import yaml

from plugins.newsEveryDay import get_headers
from lanzou.api import LanZouCloud
with open('config/api.yaml', 'r', encoding='utf-8') as f:
    apiYaml = yaml.load(f.read(), Loader=yaml.FullLoader)

lzy = LanZouCloud()
cookie = {'ylogin': str(apiYaml.get("蓝奏云").get("ylogin")), 'phpdisk_info': apiYaml.get("蓝奏云").get("phpdisk_info")}
code=lzy.login_by_cookie(cookie)


def lanzouFileToUrl(path):
    url=""
    def show_progress(file_name, total_size, now_size):
        percent = now_size / total_size
        bar_len = 40  # 进度条长总度
        bar_str = '>' * round(bar_len * percent) + '=' * round(bar_len * (1 - percent))
        print('\r{:.2f}%\t[{}] {:.1f}/{:.1f}MB | {} '.format(
            percent * 100, bar_str, now_size / 1048576, total_size / 1048576, file_name), end='')
        if total_size == now_size:
            print('')  # 下载完成换行

    def handler(fid, is_file):
        nonlocal url  # 声明要修改外部函数的url变量
        r=lzy.get_durl_by_id(fid)
        url=r.durl
    lzy.upload_file(path, -1, callback=show_progress,uploaded_handler=handler)
    return url
def newLogger():
    # 创建一个logger对象
    logger = logging.getLogger("Manayana")
    # 设置日志级别为DEBUG，这样可以输出所有级别的日志
    logger.setLevel(logging.DEBUG)
    # 创建一个StreamHandler对象，用于输出日志到控制台
    console_handler = logging.StreamHandler()
    # 设置控制台输出的日志格式和颜色
    logger.propagate = False
    console_format = '%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    console_colors = {
        'DEBUG': 'white',
        'INFO': 'cyan',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    }
    console_formatter = colorlog.ColoredFormatter(console_format, log_colors=console_colors)
    console_handler.setFormatter(console_formatter)
    # 将控制台处理器添加到logger对象中
    logger.addHandler(console_handler)
    # 使用不同级别的方法来记录不同重要性的事件
    '''logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')'''
    return logger
import logging
from logging import handlers
from test_tools.handle_path import log_dir


#用函数封装
def handle_log(name):
    #第一步：创建日志收集器
    test_log = logging.getLogger(name=name)

    #第二步：创建日志收集渠道
    pycharm = logging.StreamHandler()   # 控制台渠道
    file_log = handlers.TimedRotatingFileHandler(filename=log_dir, when='D', encoding='utf-8')

    #第三步：日志格式
    fmt = '【%(asctime)s-%(name)s-%(levelname)s-%(filename)s-%(funcName)s-[line:%(lineno)d】：%(message)s'
    log_fmt = logging.Formatter(fmt=fmt)

    # 设置日志输出格式【渠道】
    pycharm.setFormatter(fmt=log_fmt)
    file_log.setFormatter(fmt=log_fmt)

    # 设置日志级别【收集器】
    test_log.setLevel(logging.INFO)
    #test_log.setLevel(logging.DEBUG)
    #test_log.setLevel(logging.WARNING)

    #渠道
    test_log.addHandler(pycharm)
    test_log.addHandler(file_log)
    return test_log

# 使用项目名称
Log = handle_log(name="test_log")

Log.info(msg="test")
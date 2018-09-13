#!/usr/bin/env python
# coding=utf-8

from bottle import default_app, get, run
from beaker.middleware import SessionMiddleware
from common import logger_helper
# 设置session参数
session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 3600,
    'session.data_dir': '/tmp/sessions/simple',
    'session.auto': True
}

@get('/index/')
def callback():
    return 'Hello Python!'

# 函数主入口
if __name__ == '__main__':
    #app_argv = SessionMiddleware(default_app(), session_opts)
    #run(app=app_argv, host='0.0.0.0', port=9090, debug=True, reloader=True)
    logger_helper.log_info('测试info')
    logger_helper.log_debug('测试debug')
    logger_helper.log_error('测试错误')


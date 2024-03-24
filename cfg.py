# -*- coding:utf-8 -*-
# config.py 项目配置文件
import os


class BaseConfig:
    """项目配置基类，如果分不同开发环境，就继承此类，进行扩展"""
    # 数据库配置
    DBMS = 'mysql'              # 数据库管理系统
    USER = 'root'               # 账户
    PWD = '123456'              # 密码
    IP = 'localhost'            # 数据库所处主机IP
    PORT = '3306'               # 端口号
    DB = 'chinese_medicine'     # 数据库名称
    # Flask配置
    SQLALCHEMY_DATABASE_URI = ('{dbms}+py{dbms}://{user}:{pwd}@{ip}:{port}/{db}'
                               .format(dbms=DBMS,
                                       user=USER,
                                       pwd=PWD,
                                       ip=IP,
                                       port=PORT,
                                       db=DB))              # 数据库URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False                  # 禁止对象跟踪
    SECRET_KEY = 'XinJie Wang'                              # Session密钥(随意更改)
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))   # 项目根目录
    STATIC_FOLDER = os.path.join(BASE_DIR, 'static')        # 静态文件
    TEMPLATE_FOLDER = os.path.join(BASE_DIR, 'templates')   # 模板文件
    UPLOADS_FOLDER = os.path.join(BASE_DIR, 'uploads')      # 上传文件
    CACHE_CFG = {
        'CACHE_TYPE': 'simple'
    }                                                       # 缓存配置

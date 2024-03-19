# config.py 配置文件
import os


class BaseConfig:
    DBMS = 'mysql'
    USER = 'root'
    PWD = '123456'
    IP = 'localhost'
    PORT = '3306'
    DB = 'chinese_medicine'
    SQLALCHEMY_DATABASE_URI = ('{dbms}+py{dbms}://{user}:{pwd}@{ip}:{port}/{db}'
                               .format(dbms=DBMS,
                                       user=USER,
                                       pwd=PWD,
                                       ip=IP,
                                       port=PORT,
                                       db=DB))  # 数据库URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 禁止对象跟踪
    SECRET_KEY = 'XinJie Wang'
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    STATIC_FOLDER = os.path.join(BASE_DIR, 'static')
    TEMPLATE_FOLDER = os.path.join(BASE_DIR, 'templates')
    UPLOADS_FOLDER = os.path.join(BASE_DIR, 'uploads')

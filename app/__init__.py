# -*- coding:utf-8 -*-
# __init__.py  : 初始化文件，创建Flask应用

def create_app():
    from flask import Flask
    from .cfg import BaseConfig
    from . import extends
    from . import main
    from . import error

    """flask的工厂函数"""
    # 初始化app
    app = Flask(
        __name__,
        static_folder=BaseConfig.STATIC_FOLDER,
        template_folder=BaseConfig.TEMPLATE_FOLDER
    )

    # 载入配置
    app.config.from_object(BaseConfig)

    # 初始化插件
    extends.init_app(app=app)

    # 注册蓝图
    error.init_app(app)
    main.init_app(app)

    return app

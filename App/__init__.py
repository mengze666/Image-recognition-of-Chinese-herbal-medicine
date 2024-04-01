# -*- coding:utf-8 -*-
# __init__.py  : 初始化文件，创建Flask应用

def create_app(config=None):
    from flask import Flask
    from .views import blue
    from .extends import init_extends
    from .error import error
    """flask的工厂函数"""
    if not config:
        raise Exception("请传入项目配置对象~")
    # 初始化app
    app = Flask(
        __name__,
        static_folder=config.STATIC_FOLDER,
        template_folder=config.TEMPLATE_FOLDER
    )

    # 载入配置
    app.config.from_object(config)

    # 初始化插件
    init_extends(app=app)

    # 注册蓝图
    app.register_blueprint(blueprint=blue)  # 注册业务蓝图
    app.register_blueprint(blueprint=error)  # 注册异常处理蓝图

    return app

# __init__.py  : 初始化文件，创建Flask应用
from flask import Flask
from .views import blue
from .exts import init_exts
from .error import exception


def create_app(config):
    """flask的工厂函数"""

    # 初始化app
    app = Flask(
        __name__,
        static_folder=config.STATIC_FOLDER,
        template_folder=config.TEMPLATE_FOLDER
    )

    # 载入配置
    app.config.from_object(config)

    # 初始化插件
    init_exts(app=app)

    # 注册蓝图
    app.register_blueprint(blueprint=blue)  # 注册业务蓝图
    app.register_blueprint(blueprint=exception)  # 注册异常处理蓝图

    return app

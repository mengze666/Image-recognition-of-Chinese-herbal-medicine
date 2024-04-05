# -*- coding:utf-8 -*-
# extends.py: 插件管理
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_caching import Cache

db = SQLAlchemy()
migrate = Migrate()
cache = Cache()


# 和app绑定
def init_app(app):
    from app.cfg import BaseConfig
    db.init_app(app)
    migrate.init_app(app=app, db=db)
    cache.init_app(app=app, config=BaseConfig.CACHE_CFG)

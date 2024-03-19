# extends.py: 插件管理

# 扩展是第三方插件

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_caching import Cache

db = SQLAlchemy()

migrate = Migrate()
cache = Cache(config={
    'CACHE_TYPE': 'simple'
})


# 和app绑定
def init_exts(app):
    db.init_app(app)
    migrate.init_app(app=app, db=db)
    cache.init_app(app=app)

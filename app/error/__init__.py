# -*- coding:utf-8 -*-
# app/error/__init__.py

def init_app(app):
    from .views import error_bp
    app.register_blueprint(error_bp)

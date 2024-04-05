# -*- coding:utf-8 -*-
# app/main/__init__.py

def init_app(app):
    from .urls import main_bp
    app.register_blueprint(main_bp)

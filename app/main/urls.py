# -*- coding:utf-8 -*-
# app/main/urls.py
from flask import Blueprint
from .views import (
    index,
    upload,
    baike,
    baike_flavor,
    detail,
)


# 创建蓝图对象
main_bp = Blueprint('main', __name__)

main_bp.add_url_rule('/', view_func=index, methods=['GET'])
main_bp.add_url_rule('/predict', view_func=upload, methods=['GET', 'POST'])
main_bp.add_url_rule('/baike', view_func=baike, methods=['GET', 'POST'])
main_bp.add_url_rule('/baike/<int:prop>', view_func=baike_flavor, methods=['GET', 'POST'])
main_bp.add_url_rule('/baike/detail/<string:name>', view_func=detail, methods=['GET'])

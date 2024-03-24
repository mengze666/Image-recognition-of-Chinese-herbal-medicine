# -*- coding:utf-8 -*-
# error.py 错误处理蓝图
import json
from flask import Blueprint, Response

error = Blueprint('error', __name__)


@error.app_errorhandler(404)
def error_404(err):
    """这个handler可以catch住所有abort(404)以及找不到对应router的处理请求"""
    res = {"status": 404, "message": "404错误,找不到对应router"}
    return Response(json.dumps(res), mimetype='application/json')


@error.app_errorhandler(405)
def error_405(err):
    """这个handler可以catch住所有abort(405)以及请求方式有误的请求"""
    res = {"status": 405, "message": "请求方式有误"}
    return Response(json.dumps(res), mimetype='application/json')


@error.app_errorhandler(Exception)
def error_500(err):
    """这个handler可以catch住所有的abort(500)和raise exeception."""
    res = {"status": 500, "message": "系统内部错误"}
    return Response(json.dumps(res), mimetype='application/json')


class MyError(Exception):
    """自定义错误类"""
    pass

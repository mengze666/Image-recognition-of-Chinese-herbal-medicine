# -*- coding:utf-8 -*-
# app/error/views.py
import json
from flask import Response, Blueprint

from . import defines

error_bp = Blueprint('error', __name__)


@error_bp.app_errorhandler(defines.CODE_404)
def error_404(err):
    """处理 404 错误"""
    res = {"status": 404, "message": str(err)}
    return Response(json.dumps(res), mimetype='application/json'), 404


@error_bp.app_errorhandler(defines.CODE_405)
def error_405(err):
    """处理 405 错误"""
    res = {"status": 405, "message": str(err)}
    return Response(json.dumps(res), mimetype='application/json'), 405


@error_bp.app_errorhandler(Exception)
def error_500(err):
    """处理 500 错误"""
    res = {"status": 500, "message": str(err)}
    return Response(json.dumps(res), mimetype='application/json'), 500
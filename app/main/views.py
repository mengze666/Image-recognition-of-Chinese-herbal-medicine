# -*- coding:utf-8 -*-
# app/main/views.py
from flask import request, render_template

from app.extends import cache
from app.utils.predict import do_predict
from app.services.medicine import (
    query_medicines,
    query_special_medicines,
    query_medicine_by_chinese
)

import threading

lock = threading.Lock()


def index():
    return render_template('index.html')


def upload():
    if request.method == 'POST':
        with lock:
            image_file = request.files['file']
            img_bytes = image_file.read()
            res = do_predict(img_bytes)
            return render_template(
                './predict.html',
                result=res)
    elif request.method == 'GET':
        return render_template('./predict.html')


def baike():
    page = request.args.get("page", type=int, default=1)
    s = request.form.get('find', '')
    medicines, total, pagination = query_medicines(page, s)
    return render_template(
        './baike.html',
        list=medicines,
        pagination=pagination)


def baike_flavor(prop):
    page = request.args.get("page", type=int, default=1)
    s = request.form.get('find', '')
    special_medicines, total, pagination = query_special_medicines(page, prop, s)
    return render_template(
        './baike.html',
        list=special_medicines,
        pagination=pagination)


@cache.cached(timeout=60)  # 设置缓存时间，单位为秒
def detail(name):
    medicine = query_medicine_by_chinese(name)
    return render_template(
        './detail.html',
        medicine=medicine)






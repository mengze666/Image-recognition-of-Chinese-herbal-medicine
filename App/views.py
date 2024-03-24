# -*- coding:utf-8 -*-
# views.py ：视图
from flask import request, Blueprint, render_template
from flask_paginate import Pagination, get_page_parameter
from sqlalchemy import and_
from .utils import predict
# 必须在views中引入models中的全部内容
from .models import *

import os
import uuid
import cfg

blue = Blueprint('medicine', __name__)


@blue.route('/index', methods=['GET'])
@blue.route('/', methods=['GET'])
def index():
    # 主页
    return render_template('index.html')


@blue.route('/predict', methods=["POST", "GET"])
def upload():
    if request.method == 'POST':
        f0 = request.files['file']
        file_path = os.path.join(cfg.BaseConfig.UPLOADS_FOLDER + '/predict',
                                 '{}.{}'.format(uuid.uuid4(), f0.filename.split('.')[-1]))
        f0.save(file_path)
        res = predict(file_path)
        return render_template('./predict.html', result=res)
    elif request.method == 'GET':
        return render_template('./predict.html', result={})
    return render_template('./error.html')


@blue.route('/baike', methods=['GET', 'POST'])
def baike():
    page_size = 24  # 每页显示的记录条数
    # 获取页码 默认为1 int类型
    page = request.args.get(get_page_parameter(), type=int, default=1)
    start = (page - 1) * page_size  # limit后第一个参数 每一页开始位置
    end = start + page_size  # limit后第二个参数 每一页结束位置
    if request.method == 'POST':
        s = request.form['find']
        total = Medicine.query.filter(
            Medicine.chinese.like('%{}%'.format(s))
        ).count()  # 总记录数
        medicines = Medicine.query.filter(
            Medicine.chinese.like('%{}%'.format(s))
        ).slice(start, end)
        pagination = Pagination(page=page,
                                per_page=page_size,
                                found=total,
                                search=True,
                                search_msg='found <span class="tag is-info is-light">{found}</span> {record_name}',
                                record_name='medicine(s)',
                                css_framework='bulma',
                                bulma_style='rounded')
    else:
        total = Medicine.query.count()  # 总记录数
        medicines = Medicine.query.slice(start, end)
        pagination = Pagination(page=page,
                                per_page=page_size,
                                total=total,
                                search=False,
                                display_msg='''
                                            from <span class="tag is-success is-light">{start}</span> to 
                                            <span class="tag is-success is-light">{end}</span>, in total 
                                            <span class="tag is-info is-light">{total}</span> {record_name}
                                            ''',
                                record_name='medicine(s)',
                                css_framework='bulma',
                                bulma_style='rounded')
    if not total:
        medicines = []

    return render_template('./baike.html',
                           list=medicines,
                           pagination=pagination, )


@blue.route('/baike/<int:prop>', methods=['GET', 'POST'])
def baike_flavor(prop):
    property_tuple = ('凉', '温', '寒', '平')
    # 分页查询所有的数据  组装数据
    page_size = 24  # 每页显示的记录条数
    # 获取页码 默认为1 int类型
    page = request.args.get(get_page_parameter(), type=int, default=1)
    start = (page - 1) * page_size  # limit后第一个参数 每一页开始位置
    end = start + page_size  # limit后第二个参数 每一页结束位置
    if request.method == 'POST':
        s = request.form['find']
        total = Medicine.query.filter(
            and_(
                Medicine.property.like('%{}%'.format(property_tuple[prop])),
                Medicine.chinese.like('%{}%'.format(s))
            )
        ).count()  # 总记录数
        special_medicines = Medicine.query.filter(
            and_(
                Medicine.property.like('%{}%'.format(property_tuple[prop])),
                Medicine.chinese.like('%{}%'.format(s))
            )
        ).slice(start, end)
        pagination = Pagination(page=page,
                                per_page=page_size,
                                search=True,
                                search_msg='found <span class="tag is-info is-light">{found}</span> {record_name}',
                                found=total,
                                record_name='medicine(s)',
                                css_framework='bulma',
                                bulma_style='rounded')

    else:
        total = Medicine.query.filter(
            Medicine.property.like('%{}%'.format(property_tuple[prop]))
        ).count()  # 总记录数
        special_medicines = Medicine.query.filter(
            Medicine.property.like('%{}%'.format(property_tuple[prop]))
        ).slice(start, end)

        pagination = Pagination(page=page,
                                per_page=page_size,
                                total=total,
                                search=False,
                                display_msg='''
                                            from <span class="tag is-success is-light">{start}</span> to 
                                            <span class="tag is-success is-light">{end}</span>, in total 
                                            <span class="tag is-info is-light">{total}</span> {record_name}
                                            ''',
                                record_name='medicine(s)',
                                css_framework='bulma',
                                bulma_style='rounded')
    if not total:
        special_medicines = []

    return render_template('./baike.html',
                           list=special_medicines,
                           pagination=pagination)


@blue.route('/baike/detail/<string:name>', methods=['GET'])
@cache.cached(timeout=30)
def detail(name):
    mdc = Medicine.query.filter(Medicine.chinese == name).first()
    # 初始化一个空字典来存储字段备注和对应的值
    medicine_dict = {}

    # 获取 Medicine 类的所有列信息
    columns = Medicine.__table__.columns

    # 遍历每个列
    for column in columns:
        # 获取列的名称（备注）和对应的值
        column_name = column.comment
        column_value = getattr(mdc, column.name)

        # 将列的名称和对应的值存储在字典中
        medicine_dict[column_name] = column_value
    return render_template('./detail.html', medicine=medicine_dict)

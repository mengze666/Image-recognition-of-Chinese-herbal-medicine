# -*- coding:utf-8 -*-
# app/services/medicine.py
from app.models import Medicine
from app.utils.page import query_pagination
from . import defines


def query_medicine_by_chinese(name):
    mdc = Medicine.query.filter(Medicine.chinese == name).first()
    medicine_dict = {}
    columns = Medicine.__table__.columns
    for column in columns:
        column_name = column.comment
        column_value = getattr(mdc, column.name)
        medicine_dict[column_name] = column_value
    return medicine_dict


def query_medicines(page, search):
    query = Medicine.query
    if search:
        query = query.filter(Medicine.chinese.like('%{}%'.format(search)))
        return query_pagination(query, page, search=search)
    return query_pagination(query, page)


def query_special_medicines(page, prop, search):
    query = Medicine.query.filter(Medicine.property.like('%{}%'.format(defines.PROPERTY_TUPLE[prop])))
    if search:
        query = query.filter(Medicine.chinese.like('%{}%'.format(search)))
        return query_pagination(query, page, search=search)
    return query_pagination(query, page)

# -*- coding:utf-8 -*-
# app/utils/page.py
from flask_paginate import Pagination
from . import defines


def query_pagination(query, page, search=False, page_size=defines.PAGE_SIZE):
    start = (page - 1) * page_size
    end = start + page_size
    total = query.count()
    results = query.slice(start, end).all()
    if search:
        pagination = Pagination(
            page=page,
            per_page=page_size,
            total=total,
            search=True,
            search_msg=defines.SEARCH_MSG,
            css_framework=defines.CSS_FRAMEWORK,
            record_name=defines.MEDICINE_RECORD_NAME,
            bulma_style=defines.BULMA_STYLE
        )
    else:
        pagination = Pagination(
            page=page,
            per_page=page_size,
            total=total,
            display_msg=defines.DISPLAY_MSG,
            css_framework=defines.CSS_FRAMEWORK,
            record_name=defines.MEDICINE_RECORD_NAME,
            bulma_style=defines.BULMA_STYLE
        )
    return results, total, pagination

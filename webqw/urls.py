#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'zhangjingjun'
__mtime__ = '2018/8/6'
# ----------Dragon be here!----------
              ┏━┓      ┏━┓
            ┏━┛ ┻━━━━━━┛ ┻━━┓
            ┃       ━       ┃
            ┃  ━┳━┛   ┗━┳━  ┃
            ┃       ┻       ┃
            ┗━━━┓      ┏━━━━┛
                ┃      ┃神兽保佑
                ┃      ┃永无BUG！
                ┃      ┗━━━━━━━━━┓
                ┃                ┣━┓
                ┃                ┏━┛
                ┗━━┓ ┓ ┏━━━┳━┓ ┏━┛
                   ┃ ┫ ┫   ┃ ┫ ┫
                   ┗━┻━┛   ┗━┻━┛
"""
from django.urls import re_path
from . import views

app_name = 'webqw'
urlpatterns = [
    # webqw
    re_path(r'^debug/$', views.debug),
    re_path(r'^debug/save', views.debug_save),
    re_path(r'^debug/del', views.debug_del),
    re_path(r'^debug/diff$', views.debug_diff),
    re_path(r'^auto(?P<page_id>\d*)$', views.auto),
    re_path(r'^auto/add$', views.auto_add),
    re_path(r'^auto/auto_detail_(?P<task_id>\d+).html$', views.auto_detail),
    re_path(r'^auto/restart$', views.auto_restart),
    re_path(r'^auto/cancel', views.auto_cancel),
    # re_path(r'^qw_req$',views.qw_req),
    # re_path(r'^qw_req_info$',views.qw_req_info),

    # re_path(r'^auto/$', views.auto),
]

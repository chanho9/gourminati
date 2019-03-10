# -*- coding: utf-8 -*-

# 한글 인코딩 문제 해결
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Blueprint

bp = Blueprint('main', __name__)

from app.main import routes

# -*- coding: utf-8 -*-

from flask import render_template

from app.main import bp
from app.db import get_db


@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
def index():
    # 모든 식당 정보 읽기
    db = get_db()
    rows = db.execute(
        'SELECT name, type, address'
        ' FROM restaurant'
    ).fetchall()

    # SQLite rows 객체의 값을 JSON 변환가능한 데이터로 변환
    restaurants = []
    for row in rows:
        restaurants.append({
            'title': row[0],
            'content': row[1],
            'address': row[2],
        })

    return render_template('index.html', restaurants=restaurants, title=u"비밀의 맛 결사단")

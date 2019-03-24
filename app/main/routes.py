# -*- coding: utf-8 -*-

from flask import current_app, render_template, g, request

from app.main import bp
from app.db import get_db

def dbFilter(rows, parking=1, cost=2):
    
    restaurants = []

    for row in rows:    
        checked=True
        #주차장 필요없음(1)
        #주차장 필요함
        if parking==0:
            if row[3]=="X":
                checked=False

        #가격대 상관없음(2)
        #~10000(0)
        if cost==0:
            if row[4]!="$":
                checked=False        
        #~20000(1)
        elif cost==1:
            if row[4]=="$$$":
                checked=False  

        if checked==True:
            restaurants.append({
                'title': row[0],
                'content': row[1],
                'address': row[2],
             })

    return restaurants 


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET'])
def index():
    # 모든 식당 정보 읽기
    db = get_db()
    rows = db.execute(
        'SELECT name, type, address, parking, cost'
        ' FROM restaurant'
    ).fetchall()

    try:
        parkingFilter=int(request.form['parkingLotRadios'])
        costFilter=int(request.form['costRadios'])
    except (ValueError, KeyError, TypeError):
        parkingFilter=1
        costFilter=2

    # SQLite rows 객체의 값을 JSON 변환가능한 데이터로 변환
    ansRestaurants = []

    ansRestaurants = dbFilter(rows, parkingFilter, costFilter)
    
    api_Key=current_app.config['KAKAO_API_KEY']
    return render_template('application.html', restaurants=ansRestaurants, title=u"비밀의 맛 결사단", api_Key=api_Key)

# -*- coding: utf-8 -*-

from flask import current_app, render_template, g, request

from app.main import bp
from app.db import get_db, init_db, create_post, get_posts

def dbFilter(rows, parking = 1, room = 1, cost = 2):
    
    restaurants = []

    for row in rows:    
        checked=True
        #주차장 필요없음(1)
        #주차장 필요함
        if parking==0:
            if row[4]=="X":
                checked=False

        #룸 필요없음(1)
        #룸 필요함
        if room==0:
            if row[6]=="X":
                checked=False

        #가격대 상관없음(2)
        #~10000(0)
        if cost==0:
            if row[5]!="$":
                checked=False        
        #~20000(1)
        elif cost==1:
            if row[5]=="$$$":
                checked=False  

        if checked==True:
            restaurants.append({
                'id': row[0],
                'title': row[1],
                'content': row[2],
                'address': row[3],
             })

    return restaurants 


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET'])
def index():
    # db업데이트 요구 확인
    try:
        spell=str(request.form['spell'])
    except (ValueError, KeyError, TypeError):
        spell='silence'
        print('맛집 문이 열렸습니다.')

    if (spell=='Alohomora' or spell=='alohomora'):
        init_db()

    spell='silence'
    # 모든 식당 정보 읽기
    print('get db now...')
    db = get_db()
    rows = db.execute(
        'SELECT id, name, type, address, parking, cost, room'
        ' FROM restaurant'
    ).fetchall()

    try:
        parkingFilter = int(request.form['parkingLotRadios'])
        roomFilter = int(request.form['roomRadios'])
        costFilter = int(request.form['costRadios'])
    except (ValueError, KeyError, TypeError):
        parkingFilter = 1
        roomFilter = 1
        costFilter = 2

    # SQLite rows 객체의 값을 JSON 변환가능한 데이터로 변환
    ansRestaurants = []

    ansRestaurants = dbFilter(rows, parkingFilter, roomFilter, costFilter)
    
    api_Key=current_app.config['KAKAO_API_KEY']

    return render_template('application.html', restaurants=ansRestaurants, title=u"비밀의 맛 결사단", api_Key=api_Key)


@bp.route('/carrier_pigeon/<int:pigeon_num>', methods=['GET', 'POST'])
@bp.route('/carrier_pigeon', methods=['GET', 'POST'])
def carrier_pigeon(pigeon_num=-1):
    #print("Hello number : "+str(pigeon_num))
  # get 인 경우에만 post 업데이트 하고 해당 내용으로 페이지 불러오기
  # 아닌 경우에는 그냥 페이지만 불러오기      

    if request.method == 'GET':
        #print('get test')
        posts = get_posts('pigeon'+str(pigeon_num))
        return render_template('carrier_pigeon.html', posts=posts, pigeon_num=str(pigeon_num))

    if request.method == 'POST':
        #print('post test')
        name = request.form.get('name')
        post = request.form.get('post')
        create_post('pigeon'+str(pigeon_num), name, post)
        posts = get_posts('pigeon'+str(pigeon_num))
        return render_template('carrier_pigeon.html', posts=posts, pigeon_num=str(pigeon_num))

    print('?여기로 들어오면 안되는데?')
    return render_template('carrier_pigeon.html')



if __name__ == '__main__':
    app.run(debug=True)

from flask import render_template

from app.main import bp
from app.db import get_db


@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
def index():
    print("!!!")

    db = get_db()
    restaurants = db.execute(
        'SELECT name, type, address'
        ' FROM restaurant'
    ).fetchall()

    title = []
    contents = []
    address = []
    for restaurant in restaurants:
        title.append(restaurant[0])
        contents.append(restaurant[1])
        address.append(restaurant[2])

    return render_template('map.html', title=title, contents=contents, adress=address)


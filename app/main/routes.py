from flask import render_template

from app.main import bp


@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
def index():
    print("!!!")
    return render_template('map.html', title=[], contents=[], adress=[])


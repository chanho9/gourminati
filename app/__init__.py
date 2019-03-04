from flask import Flask
from config import Config

import sys

leftFrame = '''<div class ="label"><span class="left"></span><span class="center">'''
centerFrame = '''</span><span class="right"></span><br><span class="left"></span><span class="center">'''
rightFrame = '''</span><span class="right"></span></div>'''
latlonFrame = '''new daum.maps.LatLng('''

# conn = pymysql.connect(host='127.0.0.1',port=6981, user='minerva', password='1q2w3e', db='gourminati', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
#
# try:
#     with conn.cursor() as cursor:
#         sql = "select * from gourminati"
#         cursor.execute(sql);
#         result = cursor.fetchall();
#         df = pd.DataFrame(result);
#         db_title = df["title"].tolist();
#         db_contents = df["contents"].tolist();
#         db_adress = df["adress"].tolist();
#
# finally:
#     conn.close()


def create_app(config_class=Config):
    app = Flask(__name__)

    try:
        app.config.from_object('config')
    except ImportError:
        app.logger.error(
            "Failed to import config"
        )
        sys.exit(1)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app

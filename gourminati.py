from flask import Flask, render_template

import sys
import pandas as pd
import pymysql

leftFrame = '''<div class ="label"><span class="left"></span><span class="center">'''
centerFrame = '''</span><span class="right"></span><br><span class="left"></span><span class="center">'''
rightFrame = '''</span><span class="right"></span></div>'''
latlonFrame = '''new daum.maps.LatLng('''

app = Flask(__name__, **kwargs)

try:
    app.config.from_object('config')
except ImportError:
    app.logger.error(
        "Failed to import config"
    )
    sys.exit(1)


conn = pymysql.connect(host='127.0.0.1',port=6981, user='minerva', password='1q2w3e', db='gourminati', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
 
try:
    with conn.cursor() as cursor:
        sql = "select * from gourminati"
        cursor.execute(sql);
        result = cursor.fetchall();
        df = pd.DataFrame(result);
        db_title = df["title"].tolist();
        db_contents = df["contents"].tolist();
        db_adress = df["adress"].tolist();

finally:
    conn.close()


app = Flask(__name__)


@app.route("/")
def template_test():
    print("!!!")
    return render_template('map.html',  title = db_title, contents = db_contents, adress = db_adress )

if __name__ == '__main__':
    app.run(host='0.0.0.0')


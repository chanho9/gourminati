import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    KAKAO_API_KEY = os.environ.get('GOURMINATI_KAKAO_API_KEY') or 'you will never guess'
    # DATA_PATH = os.environ.get('GOURMINATI_DATA_PATH')
    DATA_PATH = 'C:\\Users\\pch88\\Desktop\\gourminati\\gourminati\\guide\\db.xlsx'
    DATABASE = os.path.join(basedir, 'gourminati.db')

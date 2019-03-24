import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    KAKAO_API_KEY = os.environ.get('GOURMINATI_KAKAO_API_KEY') or 'you will never guess'
    DATABASE = os.path.join(basedir, 'gourminati.db')
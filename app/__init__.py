# -*- coding: utf-8 -*-

from flask import Flask
from config import Config

import sys


def create_app():
    print('hi')
    # Flask app 생성
    app = Flask(__name__)

    # Configure 불러오기
    try:
        app.config.from_object(Config)
    except ImportError:
        app.logger.error(
            "Failed to import config"
        )
        sys.exit(1)

    # DB 사용 준비
    print('db will be ready')
    from app.db import init_app
    init_app(app)

    # Main 페이지 라우팅 등록
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app

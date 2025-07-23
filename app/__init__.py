from flask import Flask
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Blueprintの登録
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.exam import bp as exam_bp
    app.register_blueprint(exam_bp, url_prefix='/exam')
    
    # ヘルスチェックエンドポイント
    @app.route('/health')
    def health_check():
        return {'status': 'healthy'}, 200

    return app
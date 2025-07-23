from app import create_app
import os
import logging

# ログ設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    app = create_app()
    logger.info("Flask app created successfully")
except Exception as e:
    logger.error(f"Failed to create Flask app: {e}")
    raise

@app.shell_context_processor
def make_shell_context():
    from app.data import get_all_questions
    return {'get_all_questions': get_all_questions}

# 本番環境でのエラーハンドリング
@app.errorhandler(500)
def internal_error(error):
    return 'Internal Server Error', 500

@app.errorhandler(404)
def not_found_error(error):
    return 'Not Found', 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
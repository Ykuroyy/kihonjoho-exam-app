"""
データベースの初期化スクリプト
本番環境でデータベースをセットアップするために使用
"""
from app import create_app, db
from app.models import Question, Choice, UserAnswer

def init_database():
    app = create_app()
    
    with app.app_context():
        # テーブルを作成
        db.create_all()
        print("データベーステーブルを作成しました。")
        
        # 既存のデータがあるかチェック
        if Question.query.first() is None:
            print("問題データが存在しません。seed_data.pyを実行してください。")
        else:
            print(f"既存の問題数: {Question.query.count()}")

if __name__ == "__main__":
    init_database()
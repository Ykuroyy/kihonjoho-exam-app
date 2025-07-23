from app import create_app, db
from app.models import Question, Choice

app = create_app()

def seed_database():
    with app.app_context():
        # 既存のデータを削除
        db.session.query(Choice).delete()
        db.session.query(Question).delete()
        
        # サンプル問題データ
        questions_data = [
            {
                "year": "令和7年",
                "period": "春期",
                "number": 1,
                "category": "基礎理論",
                "question_text": "2進数1011と2進数110を加算した結果を10進数で表したものはどれか。",
                "explanation": "2進数1011は10進数で11、2進数110は10進数で6です。11 + 6 = 17となります。",
                "choices": [
                    {"symbol": "ア", "text": "15", "is_correct": False},
                    {"symbol": "イ", "text": "16", "is_correct": False},
                    {"symbol": "ウ", "text": "17", "is_correct": True},
                    {"symbol": "エ", "text": "18", "is_correct": False}
                ]
            },
            {
                "year": "令和7年",
                "period": "春期",
                "number": 2,
                "category": "アルゴリズム",
                "question_text": "配列の要素を昇順に整列するアルゴリズムのうち、平均計算量がO(n log n)であるものはどれか。",
                "explanation": "クイックソートとマージソートは平均計算量がO(n log n)です。バブルソートと選択ソートはO(n²)です。",
                "choices": [
                    {"symbol": "ア", "text": "バブルソート", "is_correct": False},
                    {"symbol": "イ", "text": "クイックソート", "is_correct": True},
                    {"symbol": "ウ", "text": "選択ソート", "is_correct": False},
                    {"symbol": "エ", "text": "挿入ソート", "is_correct": False}
                ]
            },
            {
                "year": "令和7年",
                "period": "春期",
                "number": 3,
                "category": "データベース",
                "question_text": "関係データベースにおいて、表の各行を一意に識別するための属性又は属性の組を何というか。",
                "explanation": "主キー（Primary Key）は、表の各行を一意に識別するための属性または属性の組み合わせです。",
                "choices": [
                    {"symbol": "ア", "text": "外部キー", "is_correct": False},
                    {"symbol": "イ", "text": "候補キー", "is_correct": False},
                    {"symbol": "ウ", "text": "主キー", "is_correct": True},
                    {"symbol": "エ", "text": "代替キー", "is_correct": False}
                ]
            },
            {
                "year": "令和7年",
                "period": "春期",
                "number": 4,
                "category": "ネットワーク",
                "question_text": "OSI基本参照モデルの第3層に位置し、IPアドレスを用いてパケットの経路制御を行う層はどれか。",
                "explanation": "ネットワーク層（第3層）は、IPアドレスを使用してパケットの経路制御（ルーティング）を行います。",
                "choices": [
                    {"symbol": "ア", "text": "データリンク層", "is_correct": False},
                    {"symbol": "イ", "text": "ネットワーク層", "is_correct": True},
                    {"symbol": "ウ", "text": "トランスポート層", "is_correct": False},
                    {"symbol": "エ", "text": "セション層", "is_correct": False}
                ]
            },
            {
                "year": "令和7年",
                "period": "春期",
                "number": 5,
                "category": "セキュリティ",
                "question_text": "公開鍵暗号方式において、送信者が受信者に暗号化してメッセージを送る場合、使用する鍵はどれか。",
                "explanation": "公開鍵暗号方式では、送信者は受信者の公開鍵を使用してメッセージを暗号化します。受信者は自分の秘密鍵で復号します。",
                "choices": [
                    {"symbol": "ア", "text": "送信者の公開鍵", "is_correct": False},
                    {"symbol": "イ", "text": "送信者の秘密鍵", "is_correct": False},
                    {"symbol": "ウ", "text": "受信者の公開鍵", "is_correct": True},
                    {"symbol": "エ", "text": "受信者の秘密鍵", "is_correct": False}
                ]
            },
            {
                "year": "令和7年",
                "period": "春期",
                "number": 6,
                "category": "ソフトウェア",
                "question_text": "オブジェクト指向プログラミングにおいて、既存のクラスの性質を引き継いで新しいクラスを定義することを何というか。",
                "explanation": "継承（Inheritance）は、既存のクラス（親クラス）の属性やメソッドを引き継いで新しいクラス（子クラス）を定義する仕組みです。",
                "choices": [
                    {"symbol": "ア", "text": "カプセル化", "is_correct": False},
                    {"symbol": "イ", "text": "継承", "is_correct": True},
                    {"symbol": "ウ", "text": "多態性", "is_correct": False},
                    {"symbol": "エ", "text": "抽象化", "is_correct": False}
                ]
            },
            {
                "year": "令和7年",
                "period": "春期",
                "number": 7,
                "category": "ハードウェア",
                "question_text": "CPUの性能指標の一つで、1秒間に実行できる命令数を表す単位はどれか。",
                "explanation": "MIPS（Million Instructions Per Second）は、1秒間に実行できる命令数を100万単位で表したCPUの性能指標です。",
                "choices": [
                    {"symbol": "ア", "text": "FLOPS", "is_correct": False},
                    {"symbol": "イ", "text": "MIPS", "is_correct": True},
                    {"symbol": "ウ", "text": "MHz", "is_correct": False},
                    {"symbol": "エ", "text": "CPI", "is_correct": False}
                ]
            },
            {
                "year": "令和7年",
                "period": "春期",
                "number": 8,
                "category": "システム開発",
                "question_text": "ウォータフォール型開発において、要件定義の次に行われる工程はどれか。",
                "explanation": "ウォータフォール型開発では、要件定義→設計→実装→テスト→運用・保守の順序で進みます。",
                "choices": [
                    {"symbol": "ア", "text": "実装", "is_correct": False},
                    {"symbol": "イ", "text": "設計", "is_correct": True},
                    {"symbol": "ウ", "text": "テスト", "is_correct": False},
                    {"symbol": "エ", "text": "運用", "is_correct": False}
                ]
            },
            {
                "year": "令和7年",
                "period": "春期",
                "number": 9,
                "category": "プロジェクトマネジメント",
                "question_text": "プロジェクトの進捗状況を視覚的に表現し、計画と実績を比較できる図表はどれか。",
                "explanation": "ガントチャートは、プロジェクトのタスクを時系列で表示し、計画と実績の進捗を視覚的に比較できる図表です。",
                "choices": [
                    {"symbol": "ア", "text": "パレート図", "is_correct": False},
                    {"symbol": "イ", "text": "ガントチャート", "is_correct": True},
                    {"symbol": "ウ", "text": "散布図", "is_correct": False},
                    {"symbol": "エ", "text": "ヒストグラム", "is_correct": False}
                ]
            },
            {
                "year": "令和7年",
                "period": "春期",
                "number": 10,
                "category": "経営戦略",
                "question_text": "企業の強み(S)、弱み(W)、機会(O)、脅威(T)を分析する手法を何というか。",
                "explanation": "SWOT分析は、企業の内部環境（強み・弱み）と外部環境（機会・脅威）を分析する戦略立案の手法です。",
                "choices": [
                    {"symbol": "ア", "text": "PEST分析", "is_correct": False},
                    {"symbol": "イ", "text": "SWOT分析", "is_correct": True},
                    {"symbol": "ウ", "text": "3C分析", "is_correct": False},
                    {"symbol": "エ", "text": "5F分析", "is_correct": False}
                ]
            }
        ]
        
        # データベースに保存
        for q_data in questions_data:
            question = Question(
                year=q_data["year"],
                period=q_data["period"],
                number=q_data["number"],
                category=q_data["category"],
                question_text=q_data["question_text"],
                explanation=q_data["explanation"]
            )
            db.session.add(question)
            db.session.flush()  # IDを取得するため
            
            for c_data in q_data["choices"]:
                choice = Choice(
                    question_id=question.id,
                    choice_symbol=c_data["symbol"],
                    choice_text=c_data["text"],
                    is_correct=c_data["is_correct"]
                )
                db.session.add(choice)
        
        db.session.commit()
        print("サンプルデータを登録しました。")

if __name__ == "__main__":
    seed_database()
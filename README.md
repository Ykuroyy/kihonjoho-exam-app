# 基本情報技術者試験 学習アプリ

シンプルなFlaskベースの学習アプリケーションです。基本情報技術者試験の練習問題を解くことができます。

## 特徴

- **シンプル設計**: データベース不要、メモリベースの問題管理
- **セッション管理**: ブラウザセッションで解答状況を記録
- **カテゴリー別学習**: 10のカテゴリーで問題をフィルタリング
- **詳細な解説**: 各問題に解説付き
- **成績表示**: 正答率とカテゴリー別統計
- **Railway対応**: 簡単デプロイ可能

## 技術スタック

- **Backend**: Flask 3.0.3
- **Frontend**: HTML, CSS (Bootstrap不使用)
- **Server**: Gunicorn
- **Deployment**: Railway

## ローカル開発

```bash
# 仮想環境作成
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 依存関係インストール
pip install -r requirements.txt

# アプリケーション起動
python run.py
```

アプリケーションは http://localhost:5000 で起動します。

## デプロイ (Railway)

1. GitHubリポジトリを作成してコードをプッシュ
2. Railwayアカウントを作成
3. GitHubリポジトリを接続
4. 環境変数 `SECRET_KEY` を設定
5. 自動デプロイ完了

## ファイル構成

```
├── app/
│   ├── __init__.py          # Flaskアプリケーション設定
│   ├── data.py              # 問題データ (10問)
│   ├── main/                # メインページ
│   ├── exam/                # 試験機能
│   ├── templates/           # HTMLテンプレート
│   └── static/css/          # CSS
├── config.py                # 設定
├── run.py                   # アプリケーション起動
├── requirements.txt         # 依存関係
├── Procfile                 # Railway起動設定
├── gunicorn.conf.py         # Gunicorn設定
└── README.md
```

## 問題データの追加

`app/data.py` の `QUESTIONS` リストに新しい問題を追加できます。

```python
{
    "id": 11,
    "year": "令和7年",
    "period": "春期", 
    "number": 11,
    "category": "新カテゴリー",
    "question_text": "問題文",
    "explanation": "解説",
    "choices": [
        {"symbol": "ア", "text": "選択肢1", "is_correct": False},
        {"symbol": "イ", "text": "選択肢2", "is_correct": True},
        {"symbol": "ウ", "text": "選択肢3", "is_correct": False},
        {"symbol": "エ", "text": "選択肢4", "is_correct": False}
    ]
}
```

## ライセンス

MIT License
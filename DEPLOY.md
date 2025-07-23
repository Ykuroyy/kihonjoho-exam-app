# Railwayへのデプロイ手順

## 必要な環境変数

Railwayでデプロイする際は、以下の環境変数を設定してください：

1. **SECRET_KEY** (必須)
   - Flaskアプリケーションのセキュリティキー
   - 例: `your-very-secret-key-here-change-this`

2. **DATABASE_URL** (自動設定)
   - RailwayでPostgreSQLを追加すると自動的に設定されます

## デプロイ手順

1. GitHubリポジトリにコードをプッシュ
2. Railwayで新しいプロジェクトを作成
3. GitHubリポジトリを接続
4. PostgreSQLサービスを追加
5. 環境変数でSECRET_KEYを設定
6. デプロイを実行

## 初回デプロイ後の設定

デプロイ後、データベースの初期化が必要です：

```bash
# Railway CLIを使用
railway run python init_db.py    # データベーステーブル作成
railway run python seed_data.py  # サンプルデータを投入
```

または、Railwayダッシュボードから直接実行：
1. Railwayダッシュボード → サービスを選択
2. 「Deploy」タブ → 「Connect」
3. コンソールで以下を実行：
   ```
   python init_db.py
   python seed_data.py
   ```

## トラブルシューティング

- **No start command found**: Procfileまたはrailway.jsonが正しく設定されているか確認
- **Database connection error**: DATABASE_URL環境変数が設定されているか確認
- **Import error**: requirements.txtに全ての依存関係が含まれているか確認
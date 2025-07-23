# Gunicorn設定ファイル
import os

# バインドアドレスとポート
bind = f"0.0.0.0:{os.environ.get('PORT', '8000')}"

# ワーカー設定
workers = 1
worker_class = "sync"
worker_connections = 1000
timeout = 120
keepalive = 2

# ログ設定
loglevel = "info"
accesslog = "-"
errorlog = "-"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# プロセス設定
preload_app = True
max_requests = 1000
max_requests_jitter = 100

# セキュリティ
limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190
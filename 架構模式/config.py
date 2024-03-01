import os 

def get_postgres_uri(): #取得目前的組態
    host = os.environ.get('DB_HOST','localhost')
    port = 54321 if host == 'localhost' else 5432
    password = os.environ.get('DB_PASSWORD','abc123')
    user, db_name = 'allocation', 'allocation'
    return f'postgresql://{user}:{password}@{host}:{port}/{db_name}'
"""get_api_url 函數用來生成一個 API 的 URL。它首先使用 os.environ.get 函數取得環境變量 API_HOST 的值，如果變量不存在則使用預設值 'localhost'。
然後，它根據 API_HOST 的值決定使用的端口號是 5005 或 80。然後，它組合了主機地址和端口號，生成了一個 API 的 URL。"""
def get_api_url():
    host = os.environ.get('API_HOST', 'localhost')
    port = 5005 if host == 'localhost' else 80
    return f'https://{host}:{port}'
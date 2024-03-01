from flask import Flask, jsonify, request
'''Flask 是一個 Python 框架，用來快速構建 Web 應用程序。
jsonify 是 Flask 提供的一個函數，用來將 Python 對象轉換為 JSON 格式的字符串，並將其作為 HTTP 响应返回。
request 是 Flask 提供的一個物件，用來表示 HTTP 請求。它包含了請求的所有信息，像是請求方法、URL、請求參數、請求頭等。'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#sessionmaker 是一個用來創建 Session 物件的工廠函數。Session 物件表示與數據庫的交互期間，可以用來執行查詢、插入、更新、刪除等操作。
"""已經寫好的架構"""
import config
import model 
import orm
import repository

get_session = sessionmaker(bind=create_engine(config.get_postgres_uri()))
app = Flask(__name__) 
#在這個例子中，app = Flask(__name__) 語句用來創建一個 Flask 應用程序物件。
#__name__ 參數會傳遞當前模塊的名稱給 Flask，Flask 會根據模塊的名稱自動設置一些路徑。

def is_valid_sku(sku, batches): #判斷sku跟 batch 裡的對不對的上
    return sku in {b.sku for b in batches}

@app.route('/allocate', methods=['POST'])
def allocate_endpoint():
    session = get_session()
    batches = repository.SqlAlchemyRepository(session).list()
    line = model.OrderLine(
        request.json['orderid'],
        request.json['sku'],
        request.json['qty']
    )
    
    if not is_valid_sku(line.sku, batches):
        return jsonify({'message': f'Invalid sku {line.sku}'}), 400
    try:
        batchref = model.allocate(line, batches)
    except model.OutOfStock as e:
        return jsonify({'message': str(e)},400)

    session.commit()
    return jsonify({'batchref': batchref}), 201
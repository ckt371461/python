import sys
sys.path.append('../../')
from entrypoints.flask_api import *
import pytest
import config
import requests

"""暫時定義 random"""
import uuid
def random_sku():
    return uuid.uuid4()
def random_batchref():
    return uuid.uuid4()
def random_orderid():
    return uuid.uuid4()
   

#@pytest.mark.usefixtures 是一個 pytest 的標記，它可以用來指定一個或多個 fixture 在測試函數執行前需要被執行。
# fixture 是一種可以在測試函數執行前設置環境的函數。
@pytest.mark.usefixtures('restart_api') 
def test_happy_path_return_201_and_allocated_batch(add_stock):#測試能不能用
    sku, othersku = random_sku(), random_sku('other')
    earlybatch = random_batchref(1)
    laterbatch = random_batchref(2)
    otherbatch = random_batchref(3)
    add_stock([
        (laterbatch, sku, 100, '2011-01-02'),
        (earlybatch, sku, 100, '2011-01-01'),
        (otherbatch, othersku, 100, None)
    ])
    data={'orderid':random_orderid(), 'sku':sku, 'qty':3}
    url = config.get_api_url()
    r = requests.post(f'{url}/allocate',json=data)
    assert r.status_code == 201
    assert r.json()['batchref'] == earlybatch

@pytest.mark.usefixtures('restart_api')
def test_unhappy_path_return_400_and_error_message():
    unknown_sku, orderid = random_sku(), random_orderid()
    data = {'orderid':orderid, 'sku':unknown_sku, 'qty':20}
    url = config.get_api_url()
    r = requests.post(f'{url}/allocate', json=data)
    assert r.status_code == 400
    assert r.json()['message'] == f'Invalid sku {unknown_sku}'
from flask_api import *
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
def test_api_return_allocation(add_stock):#測試能不能用
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
def test_allocations_are_persisted(add_stock):#測試能否持久保存
    sku = random_sku()
    batch1, batch2 = random_batchref(1), random_batchref(2)
    order1, order2 = random_orderid(1), random_orderid(2)
    add_stock([
        (batch1, sku, 10, '2011-01-01'),
        (batch2, sku, 10, '2011-01-02')
    ])
    line1 = {'orderid':order1, 'sku':sku, 'qty':10}
    line2 = {'orderid':order2, 'sku':sku, 'qty':10}
    url=config.get_api_url()

    #order1會耗盡batch1的庫存
    r = request.post(f'{url}/allocate', json=line1)
    assert r.status_code == 201
    assert r.json()['batchref'] == batch1

    #order2應該用batch2來配貨
    r = requests.post(f'{url}/allocate', json=line2)
    assert r.status_code == 201
    assert r.json()['batchref'] == batch2

"""測試sku缺貨或不存在"""
@pytest.mark.usefixtures('restart_api')
def test_400_message_for_out_of_stock(add_stock):
    sku, small_batch, large_order = random_sku(), random_batchref(), random_orderid()
    add_stock([
        (small_batch, sku, 10, '2011-01-01')
    ])
    data = {'orderid':large_order, 'sku':sku, 'qty':20}
    url = config.get_api_url()
    r = requests.post(f'{url}/allocate', json=data)
    assert r.status_code == 400
    assert r.json()['message'] == f'Out of stock for sku {sku}'

@pytest.mark.usefixtures('restart_api')
def test_100_message_for_invalid_sku():
    unknown_sku, orderid = random_sku(), random_orderid()
    data = {'orderid':orderid, 'sku':unknown_sku, 'qty':20}
    url = config.get_api_url()
    r = requests.post(f'{url}/allocate', json=data)
    assert r.status_code == 400
    assert r.json()['message'] == f'Invalid sku {unknown_sku}'
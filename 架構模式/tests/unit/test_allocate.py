import sys
sys.path.append('../../')
from domain.model import *
import pytest
"""暫時定義 today,tomorrow,later因為書中還沒有提到"""
import datetime
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
later = today + datetime.timedelta(days=20)
"""測試一，測試是否能成功依照eta出貨"""
def test_prefers_current_stock_batches_to_shipments():
    in_stock_batch = Batch('in-stock-batch', 'RETRO-CLOCK', 100, eta=None)
    shipment_batch = Batch('shipment-batch', 'RETRO-CLOCK', 100, eta=tomorrow)
    line = OrderLine('oref', "RETRO-CLOCK", 10)

    allocate(line, [in_stock_batch, shipment_batch])
    
    assert in_stock_batch.available_quantity == 90
    assert shipment_batch.available_quantity == 100

def test_prefers_earlier_batches():
    earliest = Batch('speedy-batch', 'MINIMALIST-SPOON', 100, eta=today)
    medium = Batch('speedy-batch', 'MINIMALIST-SPOON', 100, eta=tomorrow)
    latest = Batch('speedy-batch', 'MINIMALIST-SPOON', 100, eta=later)
    line = OrderLine('oref', 'MINIMALIST-SPOON', 10)

    allocate(line, [medium, earliest, latest])

    assert earliest.available_quantity == 90 
    assert medium.available_quantity == 100
    assert latest.available_quantity == 100

def test_returns_allocated_batch_ref():
    in_stock_batch = Batch('in-stock-batch-ref', 'HIGHBROW-POSTER', 100, eta=None)   
    shipment_batch = Batch('shipment-batch-ref', 'HIGHBROW-POSTER', 100, eta=tomorrow)
    line=OrderLine('oref', 'HIGHBROW-POSTER', 10)
    allocation = allocate(line, [in_stock_batch, shipment_batch])
    assert allocation == in_stock_batch.reference

def test_raises_out_of_stock_exception_if_cannot_allocate():#測試是否因缺貨出現意外
    batch = Batch('batch1', 'SMALL-FORK', 10 ,eta=today)
    allocate(OrderLine('order1', 'SMALL-FORK', 10), [batch])
    
    with pytest.raises(OutOfStock, match='SMALL-FORK'):#因為我們沒有詳細去寫OutOfStock,所以會出錯是正常的
        allocate(OrderLine('order2', 'SMALL-FORK', 10), [batch])
"""這段程式碼使用了 pytest.raises 裝飾器，這個裝飾器會檢查接下來的程式碼是否會引發指定的例外。
在這個程式碼中，它會檢查是否會引發 OutOfStock 例外，並且會在例外的訊息中檢查是否出現了字串 'SMALL-FORK'。
如果呼叫 allocate 函式沒有引發 OutOfStock 例外，或者引發的例外的訊息不是 'SMALL-FORK'，則這個測試會失敗。"""


if __name__ == '__main__':
    test_prefers_current_stock_batches_to_shipments()
    test_prefers_earlier_batches()
    test_returns_allocated_batch_ref()
    #test_raises_out_of_stock_exception_if_cannot_allocate()
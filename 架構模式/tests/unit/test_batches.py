#1.先寫測試程式
import sys
sys.path.append('../../')
from domain.model import *
"""測試1,allocate()"""
def test_allocating_to_a_batch_reduces_the_available():#測試配貨的程式
    batch=Batch('batch-001', 'SMALL-TABLE', qty=20, eta=date.today()) #貨批:參考ID，物品名稱，數量，日期 
    line=OrderLine('order-ref', 'SMALL-TABLE', qty=2) #訂單: 編號，物品名稱，數量

    batch.allocate(line)

    assert batch.available_quantity == 18 
#assert 語法適用於斷言，錯誤會輸出錯誤訊息，用 -O 或 -OO禁用 assert 語句，以便在正式環境中運行程序時不會檢查斷言，例如：python -O test_batches.py
# 通常情況下，你只會在開發或測試時啟用斷言，這是因為斷言會增加程序的運行時間，而且在正式上線時通常已經確保了程序的正確性，不再需要斷言的檢查。

"""測試二,can_allocate"""
def make_batch_and_line(sku, batch_qty, line_qty): #產生一組貨批和訂單
    return (Batch('batch-001', sku, batch_qty, eta=date.today()),OrderLine('order-123', sku, line_qty))

def test_can_allocate_if_available_greater_than_required(): #測試貨多於訂單時能成功發貨
    large_batch, small_line = make_batch_and_line('ELEGANT-LAMP', 20, 2)
    assert large_batch.can_allocate(small_line)

def test_cannot_allocate_if_available_smaller_than_required(): #測試貨少於訂單時會出現錯誤
    small_batch, large_line = make_batch_and_line('ELEGANT-LAMP', 2, 20)
    assert small_batch.can_allocate(large_line) is False

def test_can_allocate_if_available_equal_to_required():
    batch, line = make_batch_and_line('ELEGANT-LAMP', 2, 2)
    assert batch.can_allocate(line)

def test_cannot_allocate_if_skus_do_not_match():
    batch = Batch('batch-001', 'UNCOMFORTABLE-CHAIR', 100, eta=None)
    different_sku_line = OrderLine('order-123', 'EXPENSIVE-TOASTER', 10)
    assert batch.can_allocate(different_sku_line) is False

"""測試三,deallocate"""
def test_can_only_dellocate_allocated_lines():
    batch, unallocated_line = make_batch_and_line('DECORATIVE-TRINKET', 20, 2)
    batch.deallocate(unallocated_line)
    assert batch.available_quantity == 20

"""測試四，重複提交無效"""
def test_allocation_is_idempotent():
    batch, line = make_batch_and_line('ANGULAR-DESK', 20, 2)
    batch.allocate(line)
    batch.allocate(line)
    assert batch.available_quantity == 18

if __name__ == '__main__':
    
    test_allocating_to_a_batch_reduces_the_available()
    test_can_allocate_if_available_greater_than_required()
    test_cannot_allocate_if_available_smaller_than_required()
    test_can_allocate_if_available_equal_to_required()
    test_cannot_allocate_if_skus_do_not_match()
    test_can_only_dellocate_allocated_lines()
    test_allocation_is_idempotent()

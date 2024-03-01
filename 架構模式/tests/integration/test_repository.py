import sys
sys.path.append('../../')
from domain import model
from adapters import repository

"""測試ADD"""
def test_repository_can_save_a_batch(session):
    batch = model.Batch('batch1', 'RUSTY-SOAPDISH', 100, eta=None)

    repo = repository.SqlAlchemyRepository(session)
    repo.add(batch)
    session.commit()#在這裡，我們選擇將commit放在repository外面，並由呼叫方負責

    rows = list(session.execute(
        "SELECT reference, sku, __purchased_quantity, eta FROM 'batches'"
    )) 
    assert rows == [('batch1', 'RUSTY-SOAPDISH', 100, None)]
"""測試取貨及配貨"""
def insert_order_line(session): #插入資料並取得orderline_id
    session.execute(
        'INSERT INTO order_lines (orderid, sku, qty) VALUES ("order1","GENERIC-SOFA", 12)'
    )
    [[orderline_id]] = session.execute(
        'SELECT id FROM orderlines WHERE orderid=:orderid AND sku=:sku',#這是一個使用帶有占位符的 SQL 查試語句。
        dict(orderid="order1", sku="GENERIC-SOFA") #:orderid 和 :sku 是占位符，會在執行查試時用真實的值替換。
    )
    return orderline_id

def insert_batch(session, batch_id):
    pass

def insert_allocation(session, orderline_id, batch_id):
    pass

def test_repository_can_retrieve_a_batch_with_allocation(session):
    orderline_id = insert_order_line(session)
    batch1_id = insert_batch(session, 'batch1')
    insert_batch(session, 'batch2')
    insert_allocation(session, orderline_id, batch1_id)

    repo = repository.SqlAlchemyRepository(session)
    retrieved = repo.get('batch1')

    expected = model.Batch('batch1', 'GENERIC-SOFA', 100, eta=None)
    assert retrieved == expected #batch.__eq__只會比較參考
    assert retrieved.sku == expected.sku
    assert retrieved._purchased_quantity == expected._purchased_quantity
    assert retrieved.allocations == {
        model.OrderLine('order1', 'GENERIC-SOFA', 12), #加逗號方便識別為set
    }





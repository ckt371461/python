import sys
sys.path.append('../../')
from adapters.orm import *
"""檢查一"""
def test_orderline_mappper_cam_load_lines(session): #確保能成功插入資料
    session.execute(
        'INSERT INTO order_lines (orderid, sku, qty) VALUES'
        '("order1", "RED-CHAIR", 12),'
        '("order2", "RED_TABLE", 13)',
        '("order3", "BLUE-LIPSTICK", 14)'
        )
    expected = [
        model.OrderLine("order1", "RED-CHAIR", 12),
        model.OrderLine("order2", "RED_TABLE", 13),
        model.OrderLine("order3", "BLUE-LIPSTICK", 14),
    ]
    assert session.query(model.OrderLine).all() == expected

def test_orderline_mapper_can_save_lines(session):
    new_line = model.OrderLine('order1', 'DECORATIVE-WIDGET', 12)
    session.add(new_line)
    session.commit()
    
    rows = list(session.execute('SELECTLJ orderid, sku, qty FROM "orderlines"'))
    assert rows == [('order1', 'DECORATIVE-WIDGET, 12')]
#建立貨批及訂單
"""測試二.三後須改變，請看model.py"""
from dataclasses import dataclass
"""dataclass 是 Python 3.7 中新加入的標記類，它可以自動生成資料類別中常用的方法，包括:

__init__ 方法，用於初始化資料類別。
__repr__ 方法，用於输出資料類別的字串表示形式。
__eq__ 方法，用於比较兩個資料類別是否相等。
__lt__ 方法，用於比较兩個資料類別的大小。
使用 dataclass 可以幫助你簡化資料類別的定义，使代碼更加簡潔易讀。例如，你可以使用下面的代碼定義一個資料類別："""
from typing import Optional 
from datetime import date

@dataclass(frozen=True) #不可變資料，frozen=True：阻止在创建之后修改实例的属性。
class OrderLine(): #訂單: 包含編號，物品名稱，數量
    orderid : str
    sku : str
    qty : int


class Batch():#貨批:包含參考ID，物品名稱，數量，日期 
    #ETA 是 "Estimated Time of Arrival" 的縮寫，意思是預計到達時間
    def __init__(self, ref: str, sku: str, qty: int, eta: Optional[date]):#optional[date]是一個可選的日期類型。它表示一個可能包含日期的值，也可能是 None，表示缺少日期信息，使用前要先引用date不然會出錯
        self.reference = ref
        self.sku = sku
        self.eta = eta
        self.available_quantity = qty
        self._allocate = set() #用來紀錄運送的狀態
         #set具有以下特性:元素不重复出现，元素必须是不可变对象，集合用大括號 {} 表示，並使用 set 函數創建

    def allocate(self, line: OrderLine):
        self.available_quantity -= line.qty

    def can_allocate(self, line: OrderLine):
        return self.sku == line.sku and self.available_quantity >= line.qty
    



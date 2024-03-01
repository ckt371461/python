from dataclasses import dataclass
"""dataclass 是 Python 3.7 中新加入的標記類，它可以自動生成資料類別中常用的方法，包括:

__init__ 方法，用於初始化資料類別。
__repr__ 方法，用於输出資料類別的字串表示形式。
__eq__ 方法，用於比较兩個資料類別是否相等。
__lt__ 方法，用於比较兩個資料類別的大小。
使用 dataclass 可以幫助你簡化資料類別的定义，使代碼更加簡潔易讀。例如，你可以使用下面的代碼定義一個資料類別："""
from typing import Optional 
from datetime import date
"""物件"""
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
        self._purchased_quantity = qty #_開頭指私有變量
        self._allocations = set() #用來紀錄運送的狀態
         #set具有以下特性:元素不重复出现，元素必须是不可变对象，集合用大括號 {} 表示，並使用 set 函數創建

    def can_allocate(self, line: OrderLine) -> bool:#判斷能否送貨
        return self.sku == line.sku and self._purchased_quantity >= line.qty

    def allocate(self, line: OrderLine):#加入送貨清單
        if self.can_allocate(line):
            self._allocations.add(line)
    
    def deallocate(self, line: OrderLine):#移出送貨清單
        if line in self._allocations:
            self._allocations.remove(line)

    @property  #@property 是 Python 的一個修飾器，它可以將一個方法轉換為一個屬性，使你可以像訪問一個普通屬性一樣訪問這個方法。
    def allocated_quantity(self) -> int: #查詢配貨中數量，並指定輸出為int
        return sum(line.qty for line in self._allocations)

    @property
    def available_quantity(self) -> int: #查詢貨批數量，並指定輸出為int
        return self._purchased_quantity - self.allocated_quantity

    def __gt__(self,other): #用來協助allocate函式中的sorted排序，__gt__ 是 Python 中特殊方法的名稱。它實現了對象之間的大於（>）運算符的比較
        if self.eta is None: #None始終最小，所以傳回False
            return False
        if other.eta is None: 
            return True
        return self.eta > other.eta

    def __eq__(self,other):
        if not isinstance(other,Batch): #這段程式碼檢查 other 是否為 Batch 類的實例。它使用了 Python 的內建函數 isinstance 來執行檢查。
            return False
        return other.reference == self.reference

    def __hash__(self):
        return hash(self.reference)

class OutOfStock(Exception): #處理缺貨錯誤
    pass

"""獨立的函式"""
def allocate(line: OrderLine, batches: list[Batch]) -> str:
    try:
        batch = next(b for b in sorted(batches) if b.can_allocate(line))#next() 是 Python 中的內建函數，它可以用來返回一個迭代器的下一個元素
        batch.allocate(line)
        return batch.reference
    except:
        raise OutOfStock(f'Out of stock for sku {line.sku}')
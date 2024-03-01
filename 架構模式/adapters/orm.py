'''ORM 指的是 Object-Relational Mapping，即對象關係映射。它是一種軟體設計模式，旨在在關係數據庫和面向對象程序設計語言之間建立一個抽象層。
這樣，軟件開發人員就可以使用面向對象的方式來訪問數據庫，而不必直接使用 SQL 語言。'''
from sqlalchemy.orm import mapper, relation
from ..domain import model #ORM依賴領域模型，而不是相反的情況
from sqlalchemy import MetaData,Table,Column,Integer,String

metadata = MetaData() #資料庫

order_lines = Table(
    'order_lines', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('sku', String(255)),
    Column('qty', Integer, nullable=False),
    Column('orderid', String(255))
)

def start_mappers():
    lines_mapper = mapper(model.OrderLine, order_lines)
'''start_mappers函數使用 mapper 函數將 model.OrderLine 類別映射到 order_lines 表格。
這意味著，當你創建 model.OrderLine 實例時，SQLAlchemy 會自動將該實例的屬性映射到 order_lines 表格的對應欄位，並在必要時自動進行資料庫查詢和更新操作'''
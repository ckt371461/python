import abc
from ..domain import model
"""Python會拒絕你實例化未實作其父類別定義的所有@abc.abstractclassmethod的類別
實例化是指創建一個物件（或實例）的過程。"""
class AbstractRepository(abc.ABC):

    @abc.abstractclassmethod
    def add(self, batch: model.Batch):
        raise NotImplementedError

    @abc.abstractclassmethod
    def get(self, reference) -> model.Batch:
        raise NotImplementedError

class SqlAlchemyRepository(AbstractRepository):
    
    def __init__(self,session):
        self.session = session
    
    def add(self, batch):
        self.session.add(batch)

#query 方法是 SQLAlchemy ORM 中的一個方法，可以用來執行查試。它返回一個查試對象，可以用來構造和執行查試
    def get(self, reference):
        return self.session.query(model.Batch).filter_by(reference=reference).one()#在這個示例中，類 model.Batch 被映射到資料庫中的表格。

    def list(self):
        return self.session.query(model.Batch).all()

"""建立偽repository來進行測試"""
class FakeRepository(AbstractRepository):
    
    def __init__(self, batches):
        self._batches = set(batches)

    def add(self, batch):
        self._batches.add(batch)

    def get(self, reference):
        return next(b for b in self._batches if b.reference == reference)

    def list(self):
        return list(self._batches)


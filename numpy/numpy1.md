
```
D:\冠廷\python\numpy>python
Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:
Type "help", "copyright", "credits" or "license" fo
>>> a[(0,1,2,3,4,5),(1,2,3,4,5,6)]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
>>> import numpy as np
>>> np1 = np.array([1, 2, 3])
>>> np2 = np.array([3, 4, 5])
>>> # 陣列相加
>>> print(np1 + np2) # [4 6 8]
[4 6 8]
>>>
>>> # 顯示相關資訊
>>> print(np1.ndim, np1.shape, np1.dtype) # 1 (3,)
int64 => 一維陣列, 三個元素, 資料型別
1 (3,) int32
>>>
>>> np3 = np.array([1, 2, 3, 4, 5, 6])
>>> np3 = np3.reshape([2, 3])
>>> print(np3.ndim, np3.shape, np3.dtype) # 2 (2, 3) int64
2 (2, 3) int32
>>>  np3 = np.array([1, 2, 3, 4, 5, 6])
  File "<stdin>", line 1
    np3 = np.array([1, 2, 3, 4, 5, 6])
    ^
IndentationError: unexpected indent
>>>  print(np3[2]) # 3
  File "<stdin>", line 1
    print(np3[2]) # 3
    ^
IndentationError: unexpected indent
>>> np3 = np.array([1, 2, 3, 4, 5, 6])
>>> print(np3[2]) # 3
3
>>>
```
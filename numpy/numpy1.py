# 引入 numpy 模組
import numpy as np
np1 = np.array([1, 2, 3])
np2 = np.array([3, 4, 5])

# 陣列相加
print(np1 + np2) # [4 6 8]

# 顯示相關資訊
print(np1.ndim, np1.shape, np1.dtype) # 1 (3,) int64 => 一維陣列, 三個元素, 資料型別

np3 = np.array([1, 2, 3, 4, 5, 6])
np3 = np3.reshape([2, 3])
print(np3.ndim, np3.shape, np3.dtype) # 2 (2, 3) int64

print(np3 > 3) # [False False False  True  True  True]
print(np3[np3 > 3]) # [4 5 6]
print(np3)
print(np3.sum(axis=1)) # 將 axis=1 橫向加總 [6 15]
print(np3.sum(axis=0)) # 將 axis=0 橫向加總 [5 7 9]

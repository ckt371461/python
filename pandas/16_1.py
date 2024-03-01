import pandas as pd
data=pd.read_excel(io='普化實驗資料.xlsx',sheet_name='工作表1',header=0)
#header=0 指表格的欄位名稱放在第0筆資料，如果沒有欄位名稱使用header=None
print(data.head(len(data)))
from pandas import ExcelWriter
writer=ExcelWriter('test.xlsx',engine='xlsxwriter')
data.to_excel(writer,sheet_name='sheet2')
writer.close()#這樣寫比較好，更改writer.save()为writer.close()，会自动调用save()并关闭接口
'''writer.save()
 FutureWarning: save is not part of the public API, usage can give unexpected results and will be removed in a future version'''
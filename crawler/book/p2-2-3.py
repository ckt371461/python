import xlrd
filename = 'scores.xls'
data = xlrd.open_workbook(filename)
s1=data.sheets()[0]
#s2=data.sheets()[1]
print('data=',data)
print('s1=',s1)
#print('s2=',s2)
for row in range(s1.nrows):#nrow代表工作表中也多少列資料
    print(s1.row_values(row))#row_values(n)可以取得引數n其中任一列的結果

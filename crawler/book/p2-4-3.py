import xlrd
filename = 'scores.xls'
data = xlrd.open_workbook(filename)
sheets=data.sheets()
scores = dict()
for sheet in sheets:#nrow代表工作表中也多少列資料
    rows = list()
    for i in range(sheet.nrows):
        row = dict()
        if i == 0:
            columns = sheet.row_values(i)
        else:
            for number,datum in enumerate(sheet.row_values(i)):
                row[columns[number]] = datum
            rows.append(row)
    scores[sheet.name]=rows
print(scores)



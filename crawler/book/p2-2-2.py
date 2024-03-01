import csv
filename = 'info.csv'
data = list()
with open(filename,'rt') as fp:
    rows = csv.DictReader(fp)
    for row in rows:
        data.append(dict(row))
print(data)

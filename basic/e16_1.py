import csv
text='''author,book
J R R Tolkien,The Hobbit
Lynne Truss,"Eats,Shoots & Leaves"'''
with open('books.csv','w') as infile:
    infile.write(text)

with open('books.csv','r') as outfile:
    books=csv.DictReader(outfile)
    for book in books:
        print(book)

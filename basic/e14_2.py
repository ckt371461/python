test1='This is a test of the emergency test system'
with open('text.txt','wt') as fout:
    fout.write(test1)
with open('text.txt','rt') as fin:
    test2=fin.read()
    print(test1==test2)


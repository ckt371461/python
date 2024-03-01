from collections import OrderedDict
plain={
    'a':1,
    'b':2,
    'c':3
}
#比較dict 和 OrderDict的差別
fancy=OrderedDict([
    ('a',1),
    ('b',2),
    ('c',3),
    ])
print(plain)
print(fancy)
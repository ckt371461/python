def sum2d(list2d):
    y = 0
    for a in list2d:
        for b in a:
            y = y + b
    return  y
      
        
print('sum2d([[1,2],[3,4]])=', sum2d([[1,2],[3,4]]))

'''
[
    [1,2],
    [3,4]
]
'''

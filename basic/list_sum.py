def sum(list):
    y = 0
    for x in list:
        y = y + x
    return y         

a=3

print('sum([1,2,3])=', sum([1,2,3]))

print('sum([1,2,3,4,4])=', sum([1,2,3,4,4]))

print('sum([])=', sum([]))

print('sum([a,a,a])=', sum([a,a,a]))

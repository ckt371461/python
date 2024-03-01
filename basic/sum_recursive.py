def sum(n):
    if n==0:
        return 0
    print('n=', n)
    result = sum(n-1)+n
    print('result=', result, '= sum(', n-1, ')+', n)
    return result

print('sum(10)=', sum(10))

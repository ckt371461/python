def rangeSearch (a,v,from_,to_):
    if (from_ > to_): return -1
    mid =int((from_+to_)/2)
    if a[mid]==v:return mid
    elif v < a[mid]:
        return rangeSearch(a,v,from_,mid-1)
    else:
        return rangeSearch(a,v,mid+1,to_)

def search(a, v):
    return rangeSearch(a, v, 0, len(a)-1)

a=[1,2,3,5,8,9,11,13]
print('search(-5)=', search(a,-5))
print('search(1)=', search(a,1))
print('search(2)=', search(a,2))
print('search(6)=', search(a,6))
print('search(12)=', search(a,12))
print('search(15)=', search(a,15))

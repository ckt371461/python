def search (a,v,from_,to_):
    k =int((from_+to_)/2)
    if (k<=from_ and a[k]!=v) or k > to_:return "ˊ無解"
    elif a[k]==v:return k
    elif a[k]>v:
        to_=k
        return search(a,v,from_,to_)
    else:
        from_=k 
        return search(a,v,from_,to_)
a=[1,2,3,5,8]
print(search(a,-5,0,len(a)))
print(search(a,2,0,len(a)))
print(search(a,6,0,len(a)))
print(search(a,12,0,len(a)))

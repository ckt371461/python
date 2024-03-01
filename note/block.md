# 程式塊呈現
### python
```py
def search (a,v):
    k =int(len(a)/2)
    while(1) :
        if (k<=0 and a[k]!=v) or k > len(a):return "ˊ無解"
        elif a[k]==v:return k
        elif a[k]>v:k=int(k/2)
        else: k+=int(k/2)
print(search([1,2,3,5,8],2))
```

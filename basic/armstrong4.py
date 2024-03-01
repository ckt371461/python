def armstrong(b,l): 
    t = 0
    for d in range(b,l+1):
        k = d
        s = []
        while k >= 10:
            t = k % 10 
            k = int((k-t)/10)
            s.append(t)
            
        s.append(k)
            #print("k =:" ,k,"t =:",t)
        sum = 0
        for f in s:
            sum = f**len(str(d)) + sum
        print('sum=', sum)
        if sum == d:
            print(d)


armstrong(50,51)

# armstrong(50,200)

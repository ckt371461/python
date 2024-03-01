
def dot(x,y):
    Z = [[]]*len(x)
    for i in range(len(x)):
        Z[i] = [0]*len(y[0])
        for j in range(len(y)):
            for k in range(len(y[0])):
                Z[i][k] += x[i][j] * y[j][k]
    return(Z)
    
X = [[0,1],
     [1,3],
     [2,1]]

Y = [[0,2,1,3],
     [1,0,2,0]]

print(dot(X,Y))
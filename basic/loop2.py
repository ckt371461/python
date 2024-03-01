
# Program to add two matrices using nested loop

X = [[0,1],
    [1,3],
    [2 ,1]]

Y = [[0,2,1,3],
    [1,0,2,0]]
Z =[[0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]]
for i in range(len(X)):
    for j in range(len(Y)):
        for k in range(len(Y[0])):
            Z[i][k] += X[i][j] * Y[j][k]
print(Z)
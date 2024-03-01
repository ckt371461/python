def dot(A, B):
    m = len(A)
    n = len(A[0])# = len(B)
    p = len(B[0])
    C = [[]] * m
    for i in range(m):
        C[i] = [0]*p
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

A = [[1,2,3], 
     [3,2,1]]
B = [[1,2],
     [1,2],
     [1,2]]

print(dot(A,B))

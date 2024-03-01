def distance(p1,p2):
    sum = 0
    for i in range(len(p1)):
        sum += (p1[i] - p2[i])**2 
    return sum**0.5
print(distance((1,1,1,1),(2,2,2,2)))m
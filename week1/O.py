import numpy as np
n,m,x = map(int,input().split( ))

a = [[0 for col in range(m)] for row in range(n)]
b = np.zeros((n+2,m))

ary = list()
for i in range(n):
    ary = [y for y in input()]
    a[i] = ary

b[n+1] = input().split( )

b[0,x-1] = 1
i = 0
while i < n:
    j = 0
    while j < m:
        if b[i,j] != 0 :
            if a[i][j] == 'S':
                b[i+1,j-1] += b[i,j]
                b[i+1,j+1] += b[i,j]
            elif a[i][j] == 'R':
                b[i+1,j+1] += b[i,j]
            else:
                b[i+1,j-1] += b[i,j]
        j += 1
    i += 1

sum = 0
for i in range(m):
    sum += b[n,i] * b[n+1,i]   
print(int(sum))

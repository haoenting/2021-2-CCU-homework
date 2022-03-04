import numpy as np
n,m,r = map(int,input().split( ))

a = np.zeros((n,m))
b = np.zeros((m,r))

for i in range(n):
    ary = input().split( )
    a[i] = ary

for j in range(m):
    ary = input().split( )
    b[j] = ary


ans = a.dot(b)
for k in range(len(ans)):
    o = 0
    while o < r:
        print(int(ans[k,o]),end ='')
        print(" ",end = '')
        o += 1
    print('')

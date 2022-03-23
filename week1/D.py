#Description
阿里八八跟著盜賊來到山洞前，想要偷看通關密碼以進入堆滿金銀財寶的山洞裡。然而，等著他的不是「芝麻開門」
這麼小兒科的東西，而是兩個隨機矩陣的乘積！身為好隊友的你能幫他解開通關密碼嗎？

Input Format
輸入的第一行為三個整數 n, m, r (1 ≤ n, m, r ≤ 500)，代表矩陣 N 為 n × m 的陣列、矩陣 M 為 m × r 的矩陣。
接下來的 n 行，每行有 m 個整數，代表矩陣 N 的內容。
再接下來的 m 行，每行有 r 個整數，代表矩陣 M 的內容。
對於每個矩陣元素 a，−1000 ≤ a ≤ 1000。

Output Format
輸出 n 行，每行輸出以空白相隔的 r 個數，代表 N × M 的結果

Sample Input
2 3 1
1 2 3
3 2 1
1
2
3

Sample Output
14
10


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

Description
Super idol 的笑容都沒你的甜
八月正午的陽光都沒你耀眼
熱愛 105°C 的你
滴滴清纯的 n 個正整數，請判斷它們是不是質數。
請設計一個 isP rime(x) 函式實作此題

Input Format
輸入的第一行為一個正整數 n (1 ≤ n ≤ 100)，代表輸入的數字數量。
第二行有 n 個正整數 a1, a2, ..., an (1 ≤ ai ≤ 109
, ∀i ∈ {1, 2, ..., n})

Output Format
對於每個 ai 輸出一行，若其為質數則輸出 True ，否則輸出 False (大小寫皆可)。

Sample Input 
3 
3 4 5 

Sample Output
True
False
True

def isPrime(x):
    bool = True
    if x == 1:
        bool = False
    elif x % 2 == 0 and x != 2:
        bool = False
    else:
        i = 3
        while i <= x ** 0.5 :
            if x % i == 0:
                bool = False
                break
            i += 1
    print(bool)

n = int(input())
num = input().split( )
for j in range(n):
    isPrime(int(num[j]))

for i in range(0,n):
    isPrime(int(x[i]))

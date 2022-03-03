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

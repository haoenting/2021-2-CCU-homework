x,y = input().split( )
ary = input().split( )
ans = list(map(int,ary))
ans.sort()
num = 0
count = int(y)
while num < count:
    a = int(input())
    print(ans[a-1])
    num+=1

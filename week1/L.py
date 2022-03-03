x,y = input().split( )
set = set(input().split( ))
for i in range(int(y)):
    num = input()
    if num in set:
        print("Yes")
    else:
        print("No")

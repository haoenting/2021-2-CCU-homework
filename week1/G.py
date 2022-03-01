ary = input()
result = [a for a in ary]
num = 0
x,y = 0,0
while result[num] != 'X':
    if result[num] == 'U':
        y += 1
    elif result[num] == 'D':
        y -= 1
    elif result[num] == 'L':
        x -= 1
    else:
        x += 1
    num += 1
print(x,y)

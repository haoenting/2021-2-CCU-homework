x,y = input().split( )
y = y.lower()

i,j = 0,0
while i < len(x):
    num = ord(x[i]) + ord(y[j]) - 97

    if ord(x[i]) < 91 and num > 90:
        num -= 26
    if num > 122:
        num -= 26

    print(chr(num),end ='')
    j += 1

    if j == len(y):
        j = 0

    i += 1

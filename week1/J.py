import sys

def turn(x,y):
    ary = list()
    if y == 10 or x == 0:
        print(x)
    else:
        while x != 0:
            num = x % y
            if num > 35:
                ary.append(chr(num+29))
            elif num > 9:
                ary.append(chr(num+87))
            else:
                ary.append(num)

            x //= y

    ary.reverse()
    for i in range(len(ary)):
        print(ary[i],end = '')

    print("\n")


for line in sys.stdin:
    a,b = line.split( )
    turn(int(a),int(b))

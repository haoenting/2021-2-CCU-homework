import sys
ary = list()
num = 0
for line in sys.stdin:
    ary.append(line)
    num += 1
ary.sort()

count =0
while count < num:
    print(ary[count],end ='')
    count += 1

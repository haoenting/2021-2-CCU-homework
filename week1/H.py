import sys
for line in sys.stdin:
    if line != '\n':
        num = map(int,line.split( ))
        print(sum(num))

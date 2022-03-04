import sys
total = int(input())

BookName = list()
Bookname = list()
Code = list()
Price = list()

def books(i):
    BookName.append(input())
    Bookname.append(BookName[i].lower())
    Code.append(input())
    Price.append(input())
    

def search(line,num):
    print("case ",num,":",sep ='')
    found = False
    if ord(line[0]) > 64:
        for j in range(total):
            if line[0:len(line)-1] == Bookname[j][0:len(line)-1]:
                print(BookName[j],Code[j],Price[j],sep='\n')
                found = True

    else:
        for i in range(total):
            if line[0:len(line)-1] == Code[i][0:len(line)-1]:
                print(BookName[i],Code[i],Price[i],sep='\n')
                found = True

    if found == False:
        print("NULL")
    num += 1

for i in range(total):
    books(i)
num = 0
for line in sys.stdin:
    num += 1
    line = line.lower()
    search(line,num)
    

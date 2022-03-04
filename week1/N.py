ary1 = list(input())
ary2 = list(input())
ary3 = list(input())

LH,YF,i,j= 0,0,0,0
while i < 3:
    if ary1[i] == 'O':
        j += 1
    else:
        j -= 1
    if ary2[i] == 'O':
        j += 1
    else:
        j -= 1
    if ary3[i] == 'O':
        j += 1
    else:
        j -= 1
    i += 1

if j > 1 or j < -1:
    print("Cheat")

else:
    if ary1[0] == ary1[1] and ary1[0] == ary1[2]:
        if ary1[0] == 'O':
            LH += 1
        else:
            YF += 1
    if ary2[0] == ary2[1] and ary2[0] == ary2[2]:
        if ary2[0] == 'O':
            LH += 1
        else:
            YF += 1
    if ary3[0] == ary3[1] and ary3[0] == ary3[2]:
        if ary3[0] == 'O':
            LH += 1
        else:
            YF += 1

    if ary1[0] == ary2[0] and ary1[0] == ary3[0]:
        if ary1[0] == 'O':
            LH += 1
        else:
            YF += 1
    if ary1[1] == ary2[1] and ary1[1] == ary3[1]:
        if ary1[1] == 'O':
            LH += 1
        else:
            YF += 1
    if ary1[2] == ary2[2] and ary1[2] == ary3[2]:
        if ary1[2] == 'O':
            LH += 1
        else:
            YF += 1

    if ary1[0] == ary2[1] and ary1[0] == ary3[2]:
        if ary1[0] == 'O':
            LH += 1
        else:
            YF += 1

    if ary1[2] == ary2[1] and ary1[2] == ary3[0]:
        if ary1[2] == 'O':
            LH += 1
        else:
            YF += 1

    if LH != 0 and YF != 0:
        print("Cheat")
    elif (LH + YF) == 0:
        print("Tie")
    elif LH > YF:
        print("LH win")
    else:
        print("YF win")

ary = list(input().split( ))

for n in range(len(ary)):
    ary[n] = ary[n].lower()

ans = list(set(ary))
ans.sort()

for i in range(len(ans)):
    sum = 0
    for j in range(len(ary)):
        if ans[i] == ary[j]:
            sum += 1

    print(ans[i],sum)

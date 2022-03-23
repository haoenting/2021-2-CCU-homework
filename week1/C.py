/*
Description
助教阿元剛改完同學的期中考卷。為了登記成績方便，他想要先把考卷上的英文名字照字典序排列。
字典序即在英文字典中，排列單詞的順序。其是先按照第一個字母以升序排列（即 a、b、c⋯⋯z 的順序）。如果第
一個字母一樣，那麼比較第二個、第三個，依此類推。如果比到最後兩個單詞不一樣長，那麼把短者排在前。

Input Format
輸入為不超過 500 的若干行，每行為一個代表一位同學名字的字串 name。
名字的第一個字元皆為大寫英文字母，後面接著 0 至 99 個小寫英文字母。

Output Format
輸出與輸入相同行數的字串，代表排序後的考卷名單。

Sample Input 
Watame 
Baelz
Watson 
Kanata 
Botan 
Sample 

Output
Baelz
Botan
Kanata
Watame
Watson
*/

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

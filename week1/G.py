Description
阿金最近跟小海還有大星找到了一個藏寶圖，只要跟著指示走就能找到寶藏。但藏寶圖內的指示實在太多，為了怕
走錯，三人決定雇你寫一支程式，幫助他們找到寶藏。
他們以一個定點為原點 O(0, 0) ，以北方為 x 軸正向，東方為 y 軸正向，開始從頭依序遵循指示前進。
藏寶圖上的指示共有 5 種，分別為”U”, ”D”, ”L”, ”R”, ”X”。設三人當前位置為 (x, y)，則當指示為”U” 時，三人
會前往 (x, y + 1) 的位置；指示為”D” 時，會前往 (x, y − 1)；指示為”L” 時，會前往 (x − 1, y)；指示為”R” 時，會
前往 (x + 1, y)。指示”X” 表示已經到達寶藏的位置。

Input Format
輸入為一行連續字元，表示藏寶圖的指示。指示中必定包含唯一一個”X”。

Output Format
依序輸出兩個數字 X, Y ，分別代表寶藏的 x 座標及 y 座標。

Sample Input 
RUURDDRDLLLLUX

Sample Output
-1 0

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

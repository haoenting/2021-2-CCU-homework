/*Description
最近班上需要不少同學出公差。為了能夠適才適用，老師決定依工作的粗重程度派不同由矮到高的身高順位的同學
幫忙。
但每次都要重數實在太麻煩，因此老師請你幫忙找出需要的身高。

Input Format
輸入的第一行有兩個整數 n, q (1 ≤ n, q ≤ 500)，分別代表班上有幾位同學以及老師想派同學出多少次公差。
第二行有 n 個整數 hi (1400 ≤ hi ≤ 2000, ∀i ∈ {1, 2, ..., n})，代表班上同學的身高 (毫米)。
接下來的 q 行，每行為一個整數 rj (1 ≤ rj ≤ n, ∀j ∈ {1, 2, ..., q})，代表老師需要第 rj 高的身高。

Output Format
對於老師的每次要求，輸出一個整數，代表對應順位的身高。

Sample Input 
5 4 
1900 1610 1314 2000 1900 1900
1 
3 
4
1

Sample Output
1314 
1900
1900
1314
*/
x,y = input().split( )
ary = input().split( )
ans = list(map(int,ary))
ans.sort()
num = 0
count = int(y)
while num < count:
    a = int(input())
    print(ans[a-1])
    num+=1

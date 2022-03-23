/*Description
很久很久以前，巨龍突然出現，帶來災難帶走了公主又消失不見。王國十分危險，世間誰最勇敢，一位英雄趕來，
大聲喊：
「我要帶上最好的劍，翻過最高的山，闖進最深的森林把公主帶回到面前」
國王非常高興，忙問他的姓名，年輕人想了想，他
讀入兩個浮點數 x, y 及一個整數 k ，將 x, y 兩數之和四捨五入至小數點後第 k 位後印出

Input Format
輸入有兩個浮點數 x, y (0 ≤ x, y ≤ 1000) 及一個整數 k (0 ≤ k ≤ 5)，
如題目所述，若 k = 0，則四捨五入至整數位

Output Format
輸出一個浮點數，如題目所述

Sample Input 
652.131 42.069 2 
Sample Output
694.20
*/
x,y,z = input().split( )
sum = float(x) + float(y)
z=int(z)
if z==0:
    sum+=0.5
    print(int(sum))
elif z==1:
    print('%.1f'%sum)
elif z==2:
    print('%.2f'%sum)
elif z==3:
    print('%.3f'%sum)
elif z==4:
    print('%.4f'%sum)
else:
    print('%.5f'%sum)
        

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
        

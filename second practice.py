Practice 2:
1)

import math
a=34
b=-6
c=43.3
d=4
print('a = ',a)
print('b = ',b)
print ('c =',c)
print ('d= ',d)
z=math.ceil(a)
print ('math.ceil(',c,') = ',z)
z=math.fabs(b)
print('math.fabs (',b,') = ',z)
z=math.factorial(a)
print ('math.factorial (',a,') = ',z)
z=math.floor(c)
print ('math.factorial (',c,') = ',z)
z=math.exp(b)
print ('math.exp(',b,') = ',z)
z=math.log2(a)
print ('math.log2(',a,') = ',z)
z=math.log10(c)
print ('math.log10 (',c,') = ', z)
z=math.log(d,a)
print ('math.log(',d,',',a,')= ',z)
z=math.pow(a,d)
print ('math.pow(',a,',',d,') = ',z)
z=math.sqrt(a)
print ('math.sqrt (',a,') = ',z)
       
2) import math
x=-1
print ('x = ',x)
z=math.cos(x)
print ('math.cos(',x,') =',z)
z=math.sin(x)
print ('math.sin (',x,')=',z)
z=math.tan(x)
print ('math.tan(',x,')= ',z)
z=math.acos(x)
print ('math.acos (',x,')=',z)
z=math.asin(x)
print ('math.asin (',x,') = ',z)
z=math.atan(x)
print ('math.atan (',x,') =',z)

3)
import math
x=int(input('enter the number x:'))
            
t=int(input('enter the number t:'))
        
z=(9*math.pi*t + 10*math.cos(x))/(math.sqrt(t) -math .fabs(math.sin(t)))* math.pow(math.e,x)
print("z={0:2f}".format(z))

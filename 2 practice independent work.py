2 practice, independent work

#1 task
import math
a=int(input('enter the number a:'))
b=int(input('enter the number b:'))
h=int(input('enter the number h:'))
s=((a**2 + b)*h) / (2*(a-b) + 4)
print(s)

#2 task
import math

x= float(input('enter the number x:'))
y= float(input('enter the number y:'))
h=(math.sqrt(math.cos(2*y) + math.sin(4*y) + math.sqrt(math.pow(math.e,x)) + math.pow(math.e, -x))/(math.pow((math.pow(math.e,-x) + math.pow(math.e,x)),3)*math.pow((math.sin(4*y) + math.cos(2*y)- 2),2)))
print(h)

#3-1 task
1)
import math
x= 2
y= 1
z=math.pow(math.pow(x,y),x) + math.pow(x,(math.pow(x,y))) - math.pow(x,4)
print(z)

#2) import math
x=1
y=4
z=3
h=math.pow((abs(1/math.tan(y) + 6)),1/3) + math.sqrt(math.pow((x+1),3) / (4*y - 2*z))
print(h)


#3)
import math
x=3
y=0.2
z=(5*x*y)/(math.pow(x,3) - 4) + math.exp(x**2) + math.sqrt(math.cos(y)**2- y**2)
print(z)


#4)
import math
x=3
y=5
z=math.sqrt(math.fabs(y)) + (math.atan(math.log10(x)**3))/(math.pow(x,y) - y +1)
print(z)


#3-2 task
1)import math
x=3
y=1
z=2
h= math.pow(4,x*y)- math.pow(x, y*z) + math.pow((x*y),z)
print(h)

#2)
import math
x=2
y=2
z=1
h= (4*math.fabs(x) - x*y*(z**2))/(x+ math.exp(y*x) - 2*y*z)
print(h)
 
#3)
import math
x=0.8
y=0.1
z=4
h=(math.sqrt( math.pow(1-x + math.atan(x-7*y), 1/5 )))/(4*x*z - (math.log10(y)**2))
print(h)

#4)
import math
x=3
y=1
z=3
h= (2*3*4)/ (math.sin(x)**3 + math.tan(y)**3) - math.sqrt(math.pow(z,x-y))
print(h)
 
#3-3 task
1)
import math
x=4
h= (math.pow( math.log10(x-3),4) + 2**x * math.sin(3*x)**2 )/ (4*x - 5.2)
print(x)

#2)
import math
x=2
y=2
z=1
h= math.sqrt(0.6 * x*y*z) + math.pow(math.pow(y,x),2) - math.exp(math.sin(2* (x**2)))
print(h) 

#3)
import math
x=0.5
y=2
h= (math.asin(x**3) - 6 )/ (8* (math.cos(4*y) - math.sin(4*x)))
print(h)

#4) 
import math
x=2
y=1
z=3
h= (math.fabs(math.log10(x)**3) + math.exp(2*x)) /(  x + 3.4) - math.atan(3/( x* y* z))**3
print(h)


Answers:
    3-1
    1)-8
    2) 2.794860255207223
    3) 8104.17380516348
    4) 2.2365206553698336
    3-2
    1) 64
    2) 0.07604830203114439
    3) 0.07512459162257872
    4) 3.3486485203885072
    3-3
    1) 4
    2) 14.85968542087318
    3) 0.6961848587143972
    4) 10.01615028976077



#2 task

import math
a=int(input('a: '))
b=int(input('b: '))
c=math.sqrt(a**2 + b**2)
S = a + b +c
A = (a*b) / 2
print("c")
print('Area of a triangle:', '%.2f' % A)
print('Perimetr of a triangle: ', '%.2f' % S)
      
#3 task
import math
a=int(input('a: '))
b=int(input('b: '))
c=int (input('c: '))
d = (b**2) - (4*a*c)
if d>0:
    answer1 = (-b - math.sqrt(d))/(2*a)
    answer2 = (-b + math.sqrt(d)) / (2*a)
    print('The answers are {0} and {1}'.format(ans1, ans2))
    print("/n")
elif d==0:
        print('The answer is ' + "/n", (-b)/(2*a))

else:
            print("No answer")

#4 task

import math
_input_ =input("please choose the shape to calculate the its area:")
if _input_ == "triangle":
    base=int(input("base of triangle:"))
    height = int(input("Height og triangle:"))
    print((height * base) /2)
elif _input_ == "rectangle":
    length = int(input("length of rectangle:"))
    width = int(input("Width of rectabgle: "))
    print(length * width)

else:
    radius=int(input("radius of circle:"))
    print(math.pi * radius**2)


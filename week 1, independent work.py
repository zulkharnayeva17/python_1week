#1 task
a=input('Your last name, first name\n ')
b= input ('How old are you?\n')
c=input('Your phone number?\n')
print ('Your name', a)
print ('Your age', b)
print('Your phone number', c)

#2
PI = 3.14
r = float(input("Enter the radius of a circle:"))
area = PI * r * r
print("Area of a circle = %.2f" %area)

#3
import math
print("changing the integer and fractional parts")
a = float(input("A: "))
integer_part = math.trunc(a)
fractional_part = math.trunc((a * 100) % 100)
print(integer_part / 100 + fractional_part)
print("")
#4
import math
A=int(input('enter the number'))
Y= (A**2/3 )+ ((A**2 + 4)/6 )+ (math.sqrt(A**2 + 4))/(4) + math.sqrt(math.pow((A**2+ 4),3))/4
print(Y)

#5
import math
x= int(input(   'guess the number'))
y=((x/5) - 8)/2
print(y)


#tasks for variables, cycles

#2.1
import math

def calculate(a, b, operation):
   result = None 

   if operation == '+':
       result = sum(a, b)
   elif operation == '-':
       result = subtract(a, b)
   elif operation == '/':
       result = divide(a, b)
   elif operation == '*':
       result = multiply(a, b)
   else:
       print('unknown operation')  
    
   return result

#2.3
def numb(n):
    if n>10 and n!=12 and n>=15 and n ==18:
        return True
    else:
        return False
print(numb(14))

#2.4
i = 34
while i < 67:
    if i % 2 != 1:
        print(i)
        i += 2

#2.6

for number in range(1,101):
     if(number!=50 and number!=99):
         print(number)

# 2.7
def printing(letter,number):
    print(letter * number)
word = str(input("Enter the word "))
number = int(input("Enter the number "))
word = tuple(word)
for letters in word:
    printing(letters , number)


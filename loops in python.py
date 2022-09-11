#working with loops in python

#1

number = int(input(" enter the number:"))
i=1
factorial =1
while i <=number:
    factorial *=i
    i+= 1
print ("factorial of", number, "equal to", factorial)

# 2
n= int(input('enter the number of elements in the sequence: '))
x=1
s=0
print(x)
for i in range (n):
    s+=x
    x/=-2
    print(x)
print(' row sum:', s)

#3
n = int(input('enter the number not less than 2\n'))
i=2
while n%i !=0:
    i+=1
print('smallest natural divisor:', i)

#Exercises:
#1
input_number = 10
x=1400
for i in range (1, input_number +1):
    print("the cost for", i," kg sweets is" , (i*x))

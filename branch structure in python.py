#branch structure in python

#if-else construct

#1 task

print (' Input A:')
A= input()
print ('Input B: ')
B=input()
if A==B:
    print ('A equals B')

else :
        print ('A is not equal to B')

 #2

a= int(input('input number:'))
if a<0:
    print (a, 'less than zero')
elif a==0:
    print (a, 'equal to zero')
else:
    print (a, 'greater than zero')

# task 3

a=input ('enter the number  ')
b=input('enter the number  ')
c= input ('enter the number ')
if a<b:
    if a<c:
        y=a
    else:
        y=c
else:
    if b<c:
        y=b
    else:
        y=c

print('minimum number: ' , 

#created 27 Dec 21
#Number Lesson
#Arithmetic Overflow Problem
a=123456789123456789*987654321987654321123
print(a)

#Arithmetic Underflow Problem 1/10000=0.0001 but Python will print 0 instead
b=1 / 10000
print(b)

#Loss of Precision Problem 10/3=3.3333333.... but Python will print 3 instead
c=10 / 3
print(c)

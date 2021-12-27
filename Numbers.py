#created 27 Dec 21
#Number Lesson
#==============================================================================

#1) Arithmetic Overflow Problem
#(multiply two long floating point numbers) result in inf(infinity)
a=12.3456789123456789*987.654321987654321123
print(a)

#Arithmetic Underflow Problem
#(Division Denominator largerr than numerator)
#Example: 1/10000=0.0001 but Python will print 0 instead 
b=1 / 10000
print(b)

#Loss of Precision Problem in (Division operator)
#Example: 10/3=3.3333333.... but Python will print 3 instead
c=10 / 3
print(c)

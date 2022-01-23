#find the largest number among three numbers
a=int(input('enter the value of first number \"a" '))
b=int(input('enter the value of second number \"b" '))
c=int(input('enter the value of third number \"c" '))

if(a>b):
    if(a>c):
        print(f"a {a} is the largest")
    else:
        print(f"c {c} is the largest")
elif(b>c):
    print(f"b {b} is the largest")
else:
    print(f"c {c} is the largest")

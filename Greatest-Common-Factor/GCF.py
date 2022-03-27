a,b=input("Enter two numbers\n").split(" ")
a=eval(a)
b=eval(b)
if b>a:
 a=a+b
 b=a-b
 a=a-b
re=a%b
while re!=0:
 b=a
 a=re
 re=a%b
print("GCF of the two numbers is",a)

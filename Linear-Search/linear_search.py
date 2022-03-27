lis=[eval(x) for x in input("Enter the numbers\n").split()]
print(lis)
sch=eval(input("Enter the element to search for\n"))
for i in lis:
 if sch==i:
  print(sch,"is present in",lis)
  a=1
  break
 else:
  a=0
if a==0:
 print(sch,"is not present in",lis)

lis=[eval(x) for x in input("Enter the numbers\n").split()]
sch=eval(input("Enter the element to search for\n"))
lis.sort()
low=0
up=len(lis)-1
mid=up//2
flag=0
while up>low:
 if lis[mid]>sch:
  up=mid-1
 elif lis[mid]<sch:
  low=mid+1
 else:
  flag=1
  break
if flag==1:
 print("present")
else:
 print("not present")

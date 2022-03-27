def main():
	n=eval(input("Enter number of integers in the list\n"))		#input number of integers in the list
	listNum=[]
	for i in range(n):
		print("Enter integer",i+1)
		listNum.append(eval(input("")))		#input n number of elements to sort

	print("\n",listNum,"\n",sep="")
	for i in range(1,n):	#sorting
		for j in range(i-1,-1,-1):
			if (listNum[j+1]<listNum[j]):
				( listNum[j], listNum[j+1] ) = ( listNum[j+1], listNum[j] )
		print(listNum,"\n")

main()
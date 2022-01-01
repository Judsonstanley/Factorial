#function
def factorial(n):
	if n==1:
		return n
	else:
		return n*factorial(n-1)


#get a number from the user
number=int(input("enter a number"))


#condition
if number<0:
	print("enter a positive integer")
	n=int(input("enter again"))
	z=factorial(n)
	print (z)
elif number==0:
	print("factorial of 0 is 1")
else:
	print("the factorial",factorial(number))




def recursion_factorial(n):
   if n == 1:
       return n
   else:
       return n*recursion_factorial(n-1)

num = 5

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recursion_factorial(num))

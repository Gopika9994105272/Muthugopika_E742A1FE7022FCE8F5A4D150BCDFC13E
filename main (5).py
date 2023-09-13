#Implement a recursion Factorial to calculate the factorial of given number#
def fact_rec(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact_rec(n-1)
print("\tRecursion Factorial")
number = int(input("\n\nEnter a value  :"))
res = fact_rec(number)


print("The factorial of {} is : {} ".format(number,res))
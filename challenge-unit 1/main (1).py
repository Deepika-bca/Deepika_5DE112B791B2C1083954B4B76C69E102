# 1.1 Implement a recursive function to calculate the factorial of a given number


#Condition for checking whether the given value or the user defined value is equal to zero or whether it can satisfy the condition

def fact_rec(n):
  if n==0:
    return 1
  else:
    return(n*fact_rec(n-1))

#the value can be get through the user using this method
num=int(input("Enter a number : "))

#the value can be implemented directly 
'''num=4'''

#it calculates the total
total=fact_rec(num)

#the value gets printed with using the print statement using the values driven from the user
print("The factorial of", num, "is", total)
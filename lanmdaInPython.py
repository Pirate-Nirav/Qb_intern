'''
Python Lambda
A lambda function is a small anonymous function
A lambda function can take any amount of arguments, but can only have one expression

Syntax

lambda arguments : expression
'''

# Add 10 to argument a, and return the result:
x = lambda a : a +10
print(x(5))

# Multiply argument a with argument b and return the result

x = lambda a,b : a*b
print(x(10,2))

'''
Why use lamda function ?
The power of lamda is better shown when you use them as a anonymous function inside another function 
Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number
'''
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
'''
Python Function
A function is a block of code which only run when it is called
You can pass data known as parameter n function
A function can return data as a result

Creating a function
'''
def my_function():
    print("Hello this is first function")

my_function()

'''
Arguments 
Information can be passed into functions as arguments 
Arguments are specified after the function name, inside the parenthesis. I can add as my arguments as I want, Just separate them with a comma.

Arguments as often shortened to args in Python.

Parameter vs Argument
A parameter is the variable listed inside the parenthesis in the function 
An argument is a value that is sent to the function when it is called. 
'''

def greet(name): # Here the name is the parameter
    print(f"Hello {name}")

greet("John") # Here the john is the argument
# So this was the argument and parameter in the python

'''
Arbitrary arguments 
When i don't know how many arguments will be there in a function at that time i will use *args 
add a `*` before the arguments. this way a function will receive the tuple of argument and can access them accordingly 
'''

def add_numbers(*args):
    total = 0
    for number in args:
        total += number
    return total

print(add_numbers(1, 2, 3, 4, 5))

'''
Keyword Arguments
When i don't how many keyword arguments will be there in a function at that time i will use **kwargs 
Inside the function , kwargs is treated like a dictionary of all the extra keyword arguments 
'''
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")

'''

Feature	        *args	                            **kwargs
Type	    Tuple	                            Dictionary
Accepts 	Positional arguments	            Keyword arguments
Usage       Example	func(1, 2, 3)	            func(name="Alice", age=30)
Inside      Function	Accessed as a tuple	    Accessed as a dictionary (kwargs[key])

we can use both the *args and **kwargs but *args will come before the **kwargs 
'''
def demo(a, *args, **kwargs):
    print("a:", a)
    print("args:", args)
    print("kwargs:", kwargs)

demo(1, 2, 3, x=10, y=20)

'''
Default parameter 
If we call the function without the parameter it will use default value
'''
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# return values, to let the function return a value use return statement
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# The pass statement: The function cannot be empty but if you keep the  function empty to avoid the error we can use the pass function
def my_function(x):
    pass

# Positional-Only Arguments
# You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
#
# To specify that a function can have only positional arguments, add , / after the arguments:

def my_function(x, /):
  print(x)
my_function(3)

# Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:

def my_function(x):
  print(x)
my_function(x = 3)

# But when adding the , / you will get an error if you try to send a keyword argument:

def my_function(x, /):
  print(x)

# my_function(x = 3) This will raise an error of positional argument

# Keyword-Only Arguments
# To specify that a function can have only keyword arguments, add *, before the arguments:

def my_function(*, x):
  print(x)

my_function(x = 3)

# Without the *, you are allowed to use positionale arguments even if the function expects keyword arguments:

def my_function(x):
  print(x)
my_function(3)

# But with the *, you will get an error if you try to send a positional argument:

def my_function(*, x):
  print(x)
# my_function(3) this will raise an error


'''
Recursion
Python also accepts function recursion, which means a defined function can call itself.
Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit
of meaning that you can loop through data to reach a result.
The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never
terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can
be a very efficient and mathematically-elegant approach to programming.
In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as
the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it
'''
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)
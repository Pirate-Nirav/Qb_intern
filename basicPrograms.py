'''
# Factorial of the number

n = int(input("Enter the number: "))
fact = 1
for i in range(1,n +1):
    if i == 0:
        print("0")
    else:
        fact *= i
print(fact)

# Using the recursion for the factorial

def factorial(n):
    return 1 if n == 0 else n *factorial(n-1)

print(factorial(6))

# Simple Interest program
def simple_interest(p, n, r):
    return (p * n * r) / 100

print(simple_interest(6, 2, 5))

# A = P(1 + R/100) t

# Compound Interest = A – P

# Where,
# A is amount
# P is the principal amount
# R is the rate and
# T is the time span

def compound_interest(price, rate, time):
    amount = price * (pow((1 + rate / 100), time))
    ci = amount - price
    return ci

print(compound_interest(10000, 10.5, 5))

# ArmStrong number
n = 153
order = len(str(n))
sum = 0
temp = n
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
if n == sum:
   print(n,"is an Armstrong number")
else:
   print(n,"is not an Armstrong number")


# Program to find the area of the circle
def circleArea(radius):
    pi = 3.14
    return pi * radius ** 2

n = int(input("Enter the radius of the circle: "))
print(circleArea(n))


# Python program to print all Prime numbers in an Interval

start = 2
end = 100

for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)

#Python program to check whether a number is Prime or not
n = int(input("Enter the number to find whether it is prime or not: "))
for i in range(2,int(n**0.5)+1):
    if n % i == 0:
        print(False)
        break
    else:
        print(True)

# Python Program for n-th Fibonacci number
n = int(input("Enter the number to get the fibonacci series: "))
a,b = 0,1
count = 0

while count < n:
    print(a)
    a,b = b,a+b
    count += 1



#Python Program for How to check if a given number is Fibonacci number?

import math
def is_perfect_sqr(x):
    s = int(math.sqrt(x))
    return s ** s == x

def is_fibonacci(n):
    return is_perfect_sqr(5 * n * n + 4) or is_perfect_sqr(5 * n * n - 4)

num =21
if is_fibonacci(num):
    print(num,"is a Fibonacci number")
else:
    print(num,"is not a Fibonacci number")
    


def nth_multiple_of_k_in_fibonacci(k, n):
    a, b = 0, 1
    count = 0

    while True:
        if a % k == 0:
            count += 1
            if count == n:
                return a
        a, b = b, a + b

# Example usage
k = 5
n = 3
result = nth_multiple_of_k_in_fibonacci(k, n)
print(f"The {n}th Fibonacci number that is a multiple of {k} is: {result}")

# Python program to print ASCII value of a character
char = "A"
ascii_value = ord(char)

print(f"The ASCII value of {char} is {ascii_value}")

#Python Program for Sum of squares of first n natural numbers

n = 5
res = n * (n + 1) * (2 * n + 1) // 6
count=0
print(res)

for i in range(1, n+1):
    j = i*i
    count += j
print(count)
'''
#Python Program for cube sum of first n natural numbers
n = 3
count=0
for i in range(1, n+1):
    j = i*i*i
    count += j
print(f"The answer is {count}")
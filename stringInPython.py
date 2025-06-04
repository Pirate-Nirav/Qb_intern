'''
x = "Hello my name x"
y= "What is your name??"
print(type(x))

#to check the length 
print(len(x))

print("Hello" in x)
print(x[2:10])
print(x[:10])

#Uppercase 

print(x.upper())

# Lowercase
print(x .lower())

# Remove white space 

print(x.strip())

# Concatentaion of string

z =x+ " " +y
print(z)

""" F- string was introduced in  the python from 3.6 . To specify as a F-String put 'f' in front of the string literal & add the curly {} brackets as a placeholder 
for variables & other operations
"""

z = f"My name is z, {y}"
print(z)

# Escape Character to print the "" words in the string add \"  \"  in the sentence to add the words 
a= "My name is \" Nirav \" "
print(a)

print(a.center(30, "o"))

'''

#Python program to check if the string is palindrome or not


str1 = "malayalam"
i, j = 0 ,len(str1) -1

is_palindrome = True

while i < j:
     if str1[i] != str1[j]:
        is_palindrome = False
        break
     i += 1
     j -= 1
if is_palindrome:
    print("Yes")
else:
    print("No")


# Doing using slicing

if str1 == str1[::-1]:
    print("Yes")
else:
    print("No")

# Reverse Words in a Given String in Python

s = "As Soon as possible"

rev_s = ' ' .join(s.split()[::-1])
print(rev_s)

# using the recursion
def reverse_words(s):
    if not s:
        return ""
    return s[-1] + " " + reverse_words(s[:-1])
reverse_wordss = reverse_words(s.split())
print(reverse_wordss)

words = s.split()

stack = []
for i in words:
    stack.append(i)

reverse_wordss = ""

while stack:
    reverse_wordss += stack.pop() + " "

reverse_wordss = reverse_wordss.strip()

print(reverse_wordss)

# Remove the words from the string

s = "hello world"
s = s.replace("l", "")
print(s)

from collections import Counter

# Input string
s = "hello world hello everyone"

# Calculate word frequencies using Counter
w_freq = Counter(s.split())

print(w_freq)
'''sequence[Start : End : Step]

Parameters:

Start: It is the starting point of the slice or substring.
End: It is the ending point of the slice or substring but it does not include the last index.
Step: It is number of steps it takes.
Python’s slice() function provides an alternative definition of slicing parameters as reusable slice objects.
These objects encapsulate slicing logic and can be applied across multiple sequences.
slice(start, stop, step)
'''

s = "abcdefghij"

print(s[0:len(s):5])#af

print(s[0:len(s) -1:1])#abcdefghi

print(s[0:6:2])#ac

print(s[-7:-4:])

data = [100, 200, 300, 400, 500]
a = data[::2]
print(a)  # [100, 300, 500]

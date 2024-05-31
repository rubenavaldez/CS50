"""
Functions and Variables lecture activities  
"""

# print("Hello, World")

# Ask user for their name.
# name = input("What's your name? ")  # input expects a string 

# Say hello to user
# print("Hello,",name) # coma automatically adds a space 

"""
Print statements on two lines, overwrite new 
Print function documentation https://docs.python.org/3/library/functions.html#print
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
* implies infinite number of arguments 
sep=' ' arguments are seperated by a space 
end='\n' ends with a new line

"""

# print("Hello, ", end="")
# print("Hello,",name, sep="???")
# print(name)

"""
positional parameters: when passing values to print these aparameters appear in order 
named parameters: optional paramters that appear at the end of print, can be referenced by name
"""

# print quoted text 

# print('Hello, "friend"')
# or 
# print("Hello, \"friend\"") # backslash is an escape character

"""
Using f string (format string)
"""
# F string
# print(f"Hello, {name}")

"""
String methods
documentation https://docs.python.org/3/library/stdtypes.html#string-methods
"""
# remove white space from the left and the right 
# name = name.strip() 
# see lstrip / rstrip to remove from just left or just right

# capitalize the first letter 
# name = name.capitalize() 

# capitalize the first letter of each word
# name = name.title()

# chain methods
# name = name.strip().title()

# chain methods to input
# name = input("What's your name? ").strip().title()  
# print(f"Hello, {name}")

# Split user's name into first name and last name
# first, last = name.split(" ")
# print(f"Hello, {first}")

"""
Integers
"""
# no decimal points in an integer 
#  operators: + + * / %












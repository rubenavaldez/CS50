# python calculator

'''
integers
'''
# x = input("What's x? ") # input is always a string

# with nested functions
# x = int(input("What's x? ")) # input is always a string
# y = input("What's y? ")
# y = int(input("What's y? "))


# convert to integers 
# z= int(x) + int(y)

# print(z)
# without z variable
# print(x + y)

'''
floats
    a number with decimal point
    a real number
    cannot represent infinite numbers precisley 
        ex: 1.3333333333333333
'''
# x = float(input("What's x? ")) # input is always a string

# y = float(input("What's y? "))

# print(x + y)

'''
round the result to nearest integer 
https://docs.python.org/3/library/functions.html#round
round(number, ndigits=None)
round(number, [, ndigits])
    take one number as an argument 
    brackets refer to something that is optional
''' 

# z = round(x + y)

# print(z)

#include commas for thousands

#print(f"{z:,}") # formats thousand with a comma


'''
divison
'''

# z = x / y

#rounded
# z = round(x / y, 2) # rounds to two digits or less

# print(z)

#round with f string
# print(f'{z:.2f}') # rounds to two digits 

'''
Return 
    returns value from a function 
'''

def main():
    x = int(input("What's x? ")) 
    
    print("x squared is", square(x))

def square(n):
    # return n * n
    # return n ** 2
    return pow(n,2)

main()























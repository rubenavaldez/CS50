# print("meow")
# print("meow")
# print("meow")

# i =  3
# while(i > 0):
#     print("meow")
#     i = i - 1

'''
While Loop
'''
# i =  0
# while(i <= 3):
#     print("meow")
#     i += 1

'''
For Loop
'''
# range returns back exactly 3 values // equal to the argument
# for i in range(3):
#     print('meow')

# _ underscore variable is used if the variable does nto matter or is not used 
# for _ in range(3):
#     print('meow')

# add a new line with \n
# print("meow\n" * 3)

# print ends with a new line by default 
# overwrite the end with""
# print("meow\n" *3, end="")


'''
With user input
'''

# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break # breaks the loop

# # pass the argument back to n
# for _ in range(n):
#     print('meow')


''' 
Using Main
'''

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print('meow')
main()

# 34:05

'''
Functions 
    def create the function
    all indented code is part of the function 
    must define a function  at the top of the file 
'''
# add a parameter 
    # assign a default value
# def hello(to="world"):
    
#     print("Hello,", to)


# hello()
# name = input("What's your name? ")

# #pass the name variable as an argument
# hello(name)

'''
    Define the main part of your code at the top of the file 
'''
def main():
    name = input("What's your name? ")
    hello(name)

def hello(to='world'):
    print("Hello,", to)

#need a function call to run main

#call main
main()
'''
Scope 
    variable only exists in the context in which you defined it
'''

# def main():
#     name = input("What's your name? ")
#     hello(name)

# def hello():
#     print("Hello,", name) # name is not defined within hello


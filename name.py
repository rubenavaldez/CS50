import sys
# sys.argv contains all arguments after the file name


# argument zero is the name of the excecuted file
# print(sys.argv[0])

# try:
#     print(f"hello, my name is", sys.argv[1])
# except IndexError:
#     print("Not enough arguments")

# if len(sys.argv) < 2:
#     sys.exit("Not enough arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")  # sys.exit will end the process

# print(f"hello, my name is", sys.argv[1])


# multiple values

if len(sys.argv) < 2:
    sys.exit("Not enough arguments")

for arg in sys.argv[1:]: # starts at arg 1 and includes everything is
                #sys.argv[1:-1] omits the first and last value
    print("Hello, my name is", arg.title())
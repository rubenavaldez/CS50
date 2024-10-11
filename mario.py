# print("#")
# print("#")
# print("#")

# for _ in range(3):
#     print("#")

# def main():
#     print_column(3)


# # def print_column(height):
# #     for _ in range(height):
# #         print("#")

# # alternative print column
# def print_column(height):
#     print("#\n" * height, end="")


# main()


# horizontal

# def main():
#     print_row(4)

# def print_row(width):
#     print("?" * width)

# main()

#square

# def main():
#     print_square(3)

# def print_square(size):

#     # for each row in square
#     for i in range(size):

#         # for each brick in row
#         for j in range(size):

#             #  print brick
#             print("#", end="")

#         print() # print blank new line
# main()
# def main():
#     print_square(3)

# def print_square(size):

#     # for each row in square
#     for i in range(size):
#         print_row(size)

        
# def print_row(width):
#     print("#" * width)


# main()

# debugging

def main():
    height =int(input("Height: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print("#" * (i + 1))

if __name__ == "__main__":
    main()
    
## step into : move into a function you created 
# step over : move to the next line
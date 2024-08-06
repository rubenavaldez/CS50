def main()-> str:
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

# def is_even(n)-> bool:
#     if n % 2 ==0:
#         return True
#     else:
#         return False

# def is_even(n)-> bool:
#     return True if n % 2 == 0 else False

# def is_even(n)-> bool:
#     return n % 2 == 0 

def is_even(n)-> bool:
    return n % 2 == 0 

main()
def main()-> str:
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n)-> bool:
    if n % 2 ==0:
        return True
    else:
        return False



main()
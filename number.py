def main():
    x= get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            # x = int(x)
            return x
        except ValueError:
            pass # pass on saying anything about the error
            
            # print("x is not an integer")
        # else:   # if try succeeds         
            # return x

    
main()    
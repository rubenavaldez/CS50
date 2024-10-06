while True:
    try:
        x = int(input("What's x? "))
        # x = int(x)
    except ValueError:
        print("x is not an integer")
    else:   # if try succeeds         
        break

    
print(f"X is {x}")
    
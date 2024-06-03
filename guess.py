'''
variables 
    containers for a value that can change over time 
'''

# guess = 10

# print(guess)

def get_guess():
    guess = int(input("Enter a guess: ")) #all inputs are strings
    return guess

def main():
    guess = get_guess()
    if guess == 50:
        print("CORRECT!")
    else:
        print("INCORRECT :(")
    # print(guess)


# print(get_guess())
main()
'''
Match Statement
    similar to switch 
    break is not necessary 
    _ is default
'''

name = input("What's your name? ")

match name:
    case "Harry" | "Ron" | "Herminone":
        print("Gryffindor")
    case "Draco":
        print("Slytherine")
    case _:  # default condition 
        print("Who?")

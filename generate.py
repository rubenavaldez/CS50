import random
# from random import choice , randint  # import just choice 

# coin = random.choice(["heads", "tails"])
# print(coin)


# number = random.randint(1,10)
# print(number)

cards= ["Jack", "Queen", "King"]

random.shuffle(cards)  # shuffles the values of the list in place 

for card in cards:
    print(card)
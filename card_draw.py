# Intentionally flawed Python program

# importing modules
import itertools, random

# make a deck of cards
deck = list(itertools.product(range(1, 14), ['Spade', 'Heart', 'Diamond', 'Club']))

# shuffle the cards
random.shuffle(deck)

# draw five cards
print("You got:")
draw_count = min(5, len(deck))
for i in range(draw_count):
    print(deck[i][0], "of", deck[i][1])

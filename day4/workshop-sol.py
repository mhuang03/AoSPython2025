import random


# Problem 1: Card
# Create the Card class, which stores a card's rank and suit.
# The rank should be an integer from 1 to 13, inclusive, where 1 represents an Ace,
# 11 represents a Jack, 12 represents a Queen, and 13 represents a King.
# The suit should be a string, either "Hearts", "Diamonds", "Clubs", or "Spades".
# The Card class should have a __str__ method that returns a string representing the card,
# such as "Ace of Spades" or "10 of Hearts".

class Card:
    def __init__(self, rank, suit):
        self.rank = rank  # 1 is Ace - 13 is King
        self.suit = suit

    def __str__(self):
        names = {
            1: "Ace",
            11: "Jack",
            12: "Queen",
            13: "King"
        }

        r = self.rank
        if r in names:
            r = names[r]

        return f"{r} of {self.suit}"

    def __repr__(self):
        return str(self)


# Problem 2: Deck
# Create the Deck class, which stores a list of Card objects, representing a standard deck of 52 cards without jokers.
# The Deck class should have a __str__ method that returns a string representing the deck,
# such as "Ace of Spades, 10 of Hearts, 2 of Clubs, ..." (52 cards in total).
# The Deck class should have a shuffle method that shuffles the deck of cards. (Use random.shuffle)
# The Deck class should have a pop method that removes and returns the top card from the deck.

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["Clubs", "Diamonds", "Hearts", "Spades"]:
            for rank in range(1, 14):
                self.cards.append(Card(rank, suit))

        self.shuffle()

    def __str__(self):
        return str(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def pop(self):
        return self.cards.pop(0)


# Problem 3: Higher/Lower
# Write a program for the Higher/Lower game, where the computer picks a random card from a shuffled deck,
# and the player has to guess whether the next card is higher, lower, or equal in rank.
# Keep track of how many correct guesses the player has made in a row, and print the score after the game.
# The player can type "higher", "lower", or "equal" to make a guess, or "quit" to end the game. Discard other inputs.
# The player wins if they guess all 52 cards correctly in a row, and they lose if they make an incorrect guess.
# Use the Card and Deck classes you created in the previous problems.

deck = Deck()
# print(deck)
prev_card = deck.pop()
count = 0
while len(deck.cards) > 0:
    guess = input(f"The previous card was {prev_card}. Is the next card higher (H), lower (L), or the same (E)? ")
    next_card = deck.pop()
    if (guess == "H" and prev_card.rank >= next_card.rank) \
            or (guess == "L" and prev_card.rank <= next_card.rank) \
            or (guess == "E" and prev_card.rank != next_card.rank):
        print(f"The next card was {next_card}. You lose.")
        break

    count += 1
    prev_card = next_card
else:
    print("You won!")

print(f"You guessed {count} in a row correctly!")

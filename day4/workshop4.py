# Problem 1: Card
# Create the Card class, which stores a card's rank and suit.
# The rank should be an integer from 1 to 13, inclusive, where 1 represents an Ace,
# 11 represents a Jack, 12 represents a Queen, and 13 represents a King.
# The suit should be a string, either "Hearts", "Diamonds", "Clubs", or "Spades".
# The Card class should have a __str__ method that returns a string representing the card,
# such as "Ace of Spades" or "10 of Hearts".



# Problem 2: Deck
# Create the Deck class, which stores a list of Card objects, representing a standard deck of 52 cards without jokers.
# The Deck class should have a __str__ method that returns a string representing the deck,
# such as "Ace of Spades, 10 of Hearts, 2 of Clubs, ..." (52 cards in total).
# The Deck class should have a shuffle method that shuffles the deck of cards. (Use random.shuffle)
# The Deck class should have a pop method that removes and returns the top card from the deck.



# Problem 3: Higher/Lower
# Write a program for the Higher/Lower game, where the computer picks a random card from a shuffled deck,
# and the player has to guess whether the next card is higher, lower, or equal in rank.
# Keep track of how many correct guesses the player has made in a row, and print the score after the game.
# The player can type "higher", "lower", or "equal" to make a guess, or "quit" to end the game. Discard other inputs.
# The player wins if they guess all 52 cards correctly in a row, and they lose if they make an incorrect guess.
# Use the Card and Deck classes you created in the previous problems.
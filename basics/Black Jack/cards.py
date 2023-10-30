import random


# Function generates and returns a random card out of the provided dictionary of cards.
def get_random_card():
    random_card = random.choice(list(Cards.cards_dictionary))
    return random_card


# Takes th card generated in get_random_card() and gets its numerical value and returns it.
def get_card_value(received_card):
    card_value = Cards.cards_dictionary[received_card]
    return card_value


# This is a dictionary with the cards that are going to be used in the game.
class Cards:
    cards_dictionary = {
        "A": 11,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10,
    }


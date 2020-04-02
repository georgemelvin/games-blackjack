"""
@ Author: George Melvin -- george.melvin@gmail.com
"""

from random import shuffle


class Card:
    """
    A class used to represent a playing card.

    Attributes:
        suit (str): The card's suit.
        rank (str): The card's rank.

    """

    SUITS = ['Clubs',
             'Diamonds',
             'Hearts',
             'Spades']
    RANKS = ['Ace',
             '2',
             '3',
             '4',
             '5',
             '6',
             '7',
             '8',
             '9',
             '10',
             'Jack',
             'Queen',
             'King']
    VALUES = {
        'Ace-lo': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Jack': 10,
        'Queen': 10,
        'King': 10,
        'Ace-hi': 11
    }

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f'{self.rank} of {self.suit}'

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def is_ace(self):
        return self.rank == 'Ace'

    def get_value(self):
        if self.is_ace():
            print('Unable to get value - this card is an Ace.')
            return
        else:
            rank = self.get_rank()
            return self.VALUES[rank]

    def echo(self):
        rank = self.rank
        suit = self.suit
        print(f'{rank} of {suit}')


class Deck:
    """
    A class used to represent a deck of cards.
    """


    def __init__(self):
        self.cards = \
            [Card(suit,value) for value in Card.RANKS for suit in Card.SUITS]

    def is_empty(self):
        cards = self.cards
        return not bool(cards)

    def get_cards(self):
        return self.cards

    def count_cards(self):
        return len(self.cards)

    def select_card(self):
        if self.is_empty():
            print('The deck is empty...!')
            return

        card = self.cards[0]
        self.cards = self.cards[1:]

        return card

    def insert_card(self, card):
        self.cards.append(card)

    def shuffle_cards(self):
        shuffle(self.cards)



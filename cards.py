"""
@ Author: George Melvin -- george.melvin@gmail.com
"""

import random


SEED = 123

SUITS = ['Clubs',
         'Diamonds',
         'Hearts',
         'Spades']
VALUES = ['Ace',
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

CARD_POINTS = {
        'Ace': 1,
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
          'King': 10
}


class Card:
    """

    """

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value

    def echo(self):
        value = self.value
        suit = self.suit
        print(f'{value} of {suit}')


class Deck:
    """

    """


    def __init__(self):
        self.cards = [Card(suit,value) for value in VALUES for suit in SUITS]

    def get_cards(self):
        return self.cards

    def select(self):
        card = self.cards[0]
        self.cards = self.cards[1:]
        card.echo()

        return card

    def insert(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)



if __name__ == '__main__':

    card = Card('Clubs', 'Jack')
    card.echo()

    deck = Deck()
    deck.shuffle()

    for i in range(10):
        deck.select()

    print(len(deck.get_cards()))


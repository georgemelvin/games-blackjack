"""
@ Author: George Melvin -- george.melvin@gmail.com
"""

from random import shuffle

import cards


class BlackjackHand:
    """
    A class used to represent a hand of cards in Blackjack.

    Attributes:
        hand_of_cards (list): A list of Card objects.
    """

    def __init__(self, hand_of_cards):
        self.hand = hand_of_cards

    def is_empty(self):
        return not bool(self.hand)

    def append_card(self, card):
        self.hand.append(card)

    def get_ranks(self):
        return [card.get_rank() for card in self.hand]

    def get_cards(self):
        return self.hand

    def get_top_card(self):
        return self.hand[0]

    def count_cards(self):
        return len(self.hand)

    def contains_ace(self):
        return 'Ace' in self.get_ranks()

    def count_aces(self):
        return sum([card.is_ace() for card in self.hand])

    def get_aces_soft_value(self):
        if not self.contains_ace():
            return 0

        aces_count = self.count_aces()

        return 11 + (aces_count-1)

    def get_aces_hard_value(self):
        if not self.contains_ace():
            return 0

        aces_count = self.count_aces()

        return aces_count

    def get_non_aces_value(self):
        non_aces_value = 0

        if self.count_cards() > self.count_aces():
            non_aces_value \
                += sum([card.get_value() for card in self.hand if not card.is_ace()])

        return non_aces_value

    def get_soft_value(self):
        aces_value = self.get_aces_soft_value()
        non_aces_value = self.get_non_aces_value()

        return aces_value + non_aces_value

    def get_hard_value(self):
        aces_value = self.get_aces_hard_value()
        non_aces_value = self.get_non_aces_value()

        return aces_value + non_aces_value

    def is_soft_bust(self):
        return self.get_soft_value() > 21

    def is_bust(self):
        return self.get_hard_value() > 21

    def is_blackjack(self):
        return (self.count_cards() == 2) and (self.get_soft_value() == 21)


class Player:
    """
    A class used to represent a Blackjack player.
    """

    def __init__(self, name=None, strategy=None):
        self.name = name
        self.hand = BlackjackHand([])
        self.strategy = strategy

    def has_empty_hand(self):
        return self.hand.is_empty()

    def show_hand(self):
        if self.has_empty_hand():
            return f'Player {self.name} has no cards...!'

        print(f'Player {self.name} has the following cards: \n')
        for card in self.hand.get_cards():
            print(card)
        print('-' * 40)

    def is_soft_bust(self):
        return self.hand.is_soft_bust()

    def is_bust(self):
        return self.hand.is_bust()

    def receive_card(self, card):
        self.hand.append_card(card)

    def get_soft_value(self):
        return self.hand.get_soft_value()

    def get_hard_value(self):
        return self.hand.get_hard_value()


class Dealer(Player):
    """
    A class used to represent a Blackjack dealer.
    """

    def __init__(self, name=None):
        self.deck = cards.Deck()
        super().__init__(name)

    def shuffle_deck(self):
        self.deck.shuffle_cards()

    def deal_card(self, player=None):
        card = self.deck.select_card()
        player.receive_card(card)

    def get_face_up(self):
        return self.hand.get_top_card()




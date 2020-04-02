"""

"""


def count_aces_in_hand(hand_of_cards):
    """ Count the number of Ace cards in a hand of cards.

    Args:
        hand_of_cards (list): A (non-empty) list of Card objects.

    Returns:
        (int): The number of Ace cards in the hand.
    """

    return sum([card.is_ace() for card in hand_of_cards])

def count_value_from_hand(hand_of_cards):
    """ Determine the value of a hand of cards in Blackjack.

    Args:
        hand_of_cards (list): A (non-empty) list of Card objects.

    Returns:
        (int): The total value of the hand.
    """

    ace_count = count_aces_in_hand(hand_of_cards)

    if ace_count == 0:
        non_ace_values = [card.get_value() for card in hand_of_cards if not card.is_ace()]
        return sum(non_ace_values)









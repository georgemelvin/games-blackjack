"""
@ Author: George Melvin -- george.melvin@gmail.com
"""

import time

from players import Player, Dealer


class BlackjackGame:
    """
    A class used to represent a game of Blackjack.

    Attributes:
        num_shuffles (int): The initial number of shuffles by the dealer.
    """

    def __init__(self, num_shuffles=1):
        self.num_shuffles = num_shuffles

        self.dealer = Dealer(name='Dealer')
        self.player = Player(name='1')
        self.game_over = False

    def initial_dealer_shuffle(self):
        dealer = self.dealer

        for k in range(self.num_shuffles):
            dealer.shuffle_deck()

        print('Dealer has shuffled the deck...')

    def initial_deal(self):
        dealer = self.dealer
        player = self.player

        self.initial_dealer_shuffle()

        for i in range(2):
                dealer.deal_card(player=player)

        for j in range(2):
            dealer.deal_card(player=dealer)

        # self.dealer_soft_total = dealer.get_soft_value()
        # self.dealer_hard_total = dealer.get_hard_value()

        print('Cards have been dealt...')

    def show_player_hand(self):
        player = self.player
        player.show_hand()

    # def get_player_soft_total(self):
    #     return self.player_soft_total
    #
    # def get_player_hard_total(self):
    #     return self.player_hard_total

    def show_dealer_hand(self):
        dealer = self.dealer
        print("Showing dealer's face down card...")
        dealer.show_hand()

    # def get_dealer_soft_total(self):
    #     return self.dealer_soft_total
    #
    # def get_dealer_hard_total(self):
    #     return self.dealer_hard_total

    def show_dealer_face_up(self):
        dealer = self.dealer
        print('Dealer has the following face up card: \n')
        print(dealer.get_face_up())
        print('-'*40)

    # def is_player_blackjack(self):
    #     player = self.player
    #
    #     return player.hand.is_blackjack()
    #
    # def is_dealer_blackjack(self):
    #     dealer = self.dealer
    #
    #     return dealer.hand.is_blackjack()

    def player_hit(self,hit=True):
        dealer = self.dealer
        player = self.player

        if player.hand.is_blackjack():
            print('Blackjack!')
            return

        while hit:
            hit_card = input('Do you want another card? (y/n)')

            if hit_card == 'y':
                dealer.deal_card(player=player)
                # self.player_soft_total = player.get_soft_value()
                # self.player_hard_total = player.get_hard_value()
                player.show_hand()

                if player.is_bust():
                    return self.end(player_total=player.get_hard_value(),
                                    player_is_bust=True)

                if (player.get_soft_value() == 21
                        or player.get_hard_value() == 21):
                    hit=False

            elif hit_card == 'n':
                player.show_hand()
                hit=False

            else:
                print('Please type y(=yes) or n(=no)')

    def dealer_hit(self, hit=True, player_total=0):
        player = self.player
        dealer = self.dealer

        if dealer.hand.is_blackjack():
            print('Blackjack!')
            if player.hand.is_blackjack:
                return self.end(player_total=player_total,
                                dealer_total=dealer.get_soft_value(),
                                is_push=True)
            else:
                return self.end(player_total=player_total,
                                dealer_total=dealer.get_soft_value(),
                                dealer_wins=True)

        if player.hand.is_blackjack():
            while hit:
                print('Dealing card for dealer...')

                dealer.deal_card(player=dealer)
                # self.dealer_soft_total = dealer.get_soft_value()
                # self.dealer_hard_total = dealer.get_hard_value()
                dealer.show_hand()

                if dealer.is_bust():
                    return self.end(dealer_total=dealer.get_hard_value(),
                                    dealer_is_bust=True)

                if (dealer.dealer_soft_total() == 21
                        or dealer.dealer_hard_total() == 21):
                    return self.end(player_total=player_total,
                                    dealer_total=21,
                                    is_push=True)

        if dealer.get_soft_value() > 17:
            if dealer.get_soft_value() > player_total:
                return self.end(player_total=player_total,
                                dealer_total=dealer.get_soft_value(),
                                dealer_wins=True)
            if dealer.get_soft_value() < player_total:
                return self.end(player_total=player_total,
                                dealer_total=dealer.get_soft_value(),
                                player_wins=True)
            if dealer.get_soft_value() == player_total:
                return self.end(player_total=player_total,
                                dealer_total=dealer.get_soft_value(),
                                is_push=True)

        if dealer.get_hard_value() > 16:
            if dealer.get_hard_value() > player_total:
                return self.end(player_total=player_total,
                                dealer_total=dealer.get_hard_value(),
                                dealer_wins=True)
            if dealer.get_hard_value() < player_total:
                return self.end(player_total=player_total,
                                dealer_total=dealer.get_hard_value(),
                                player_wins=True)
            if dealer.get_hard_value() == player_total:
                return self.end(player_total=player_total,
                                dealer_total=dealer.get_hard_value(),
                                is_push=True)

        while hit:
            print('Dealing card for dealer...')
            time.sleep(2)

            dealer.deal_card(player=dealer)
            # self.dealer_soft_total = dealer.get_soft_value()
            # self.dealer_hard_total = dealer.get_hard_value()
            dealer.show_hand()

            if dealer.is_bust():
                return self.end(dealer_total=dealer.get_hard_value(),
                                dealer_is_bust=True)

            if not dealer.is_soft_bust() and dealer.get_soft_value() > 17:
                if dealer.get_soft_value() > player_total:
                    return self.end(player_total=player_total,
                                    dealer_total=dealer.get_soft_value(),
                                    dealer_wins=True)
                if dealer.get_soft_value() < player_total:
                    return self.end(player_total=player_total,
                                    dealer_total=dealer.get_soft_value(),
                                    player_wins=True)
                if dealer.get_soft_value() == player_total:
                    return self.end(player_total=player_total,
                                    dealer_total=dealer.get_soft_value(),
                                    is_push=True)

            if not dealer.is_soft_bust() and dealer.get_hard_value() > 16:
                if dealer.get_soft_value() > player_total:
                    return self.end(player_total=player_total,
                                    dealer_total=dealer.get_soft_value(),
                                    dealer_wins=True)
                if dealer.get_soft_value() < player_total:
                    return self.end(player_total=player_total,
                                    dealer_total=dealer.get_soft_value(),
                                    player_wins=True)
                if dealer.get_soft_value() == player_total:
                    return self.end(player_total=player_total,
                                    dealer_total=dealer.get_soft_value(),
                                    is_push=True)


            if dealer.is_soft_bust() and dealer.get_hard_value() > 16:
                if dealer.get_hard_value() > player_total:
                    return self.end(player_total=player_total,
                                    dealer_total=dealer.get_hard_value(),
                                    dealer_wins=True)
                if dealer.get_hard_value() < player_total:
                    return self.end(player_total=player_total,
                                    dealer_total=dealer.get_hard_value(),
                                    player_wins=True)
                if dealer.get_hard_value() == player_total:
                    return self.end(player_total=player_total,
                                    dealer_total=dealer.get_hard_value(),
                                    is_push=True)




    def end(self, player_total=0, dealer_total=0,
            is_push=False, player_is_bust=False, dealer_is_bust=False,
            player_wins=False, dealer_wins=False):

        if player_is_bust:
            print(f'Player total: {player_total}')
            print('Player gone bust... House wins!')
            self.game_over = True
            return

        if dealer_is_bust:
            print(f'Dealer total: {dealer_total}')
            print('Dealer gone bust... You win! Congratulations.')
            self.game_over = True
            return

        if is_push:
            print(f'Player total: {player_total}')
            print(f'Dealer total: {dealer_total}')
            print("Push... At least you didn't lose!")
            self.game_over = True
            return

        if player_wins:
            print(f'Player total: {player_total}')
            print(f'Dealer total: {dealer_total}')
            print('You win! Congratulations.')
            self.game_over = True
            return

        if dealer_wins:
            print(f'Player total: {player_total}')
            print(f'Dealer total: {dealer_total}')
            print('You lost... Better luck next time!')
            self.game_over = True
            return

def play():
    # Initialize game of Blackjack
    game = BlackjackGame()
    print('-'*40)
    print('Welcome to Blackjack... Good luck!')
    print('-' * 40)

    # Dealer shuffles cards
    game.initial_dealer_shuffle()

    # Cards are dealt to Player and Dealer
    game.initial_deal()
    print('-' * 40)
    game.show_dealer_face_up()

    # Player shows their hand
    game.show_player_hand()

    # Player plays their hand
    game.player_hit()

    if game.player.is_soft_bust():
        player_total = game.player.get_hard_value()
    else:
        player_total = game.player.get_soft_value()

    if game.game_over:
        print(f'Player total: {player_total}')
        print('Game over...')
    else:
        print(f'Player total: {player_total}')
        game.show_dealer_hand()
        game.dealer_hit(player_total=player_total)

if __name__ == '__main__':
    play()










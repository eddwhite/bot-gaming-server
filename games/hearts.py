#!/bin/python3
'''
Hearts
------
Todo
----
send players what cards have been played
use proper terminology
verify players move
'''

import random


class Card:
    def __init__(self, v, s):
        self.value = v
        self.suit = s


    def __eq__(self, other):
        return self.value == other.value and self.suit == other.suit


    def __cmp__(self, other):
        if self.value > other.value:
            return 1
        elif other.value > self.value:
            return -1
        # order suits alphabetically for now
        elif self.suit > other.suit:
            return 1
        elif other.suit > self.suit:
            return -1
        else:
            return 0


class Hearts:
    def __init__(self, player_cb):
        self.hands = []
        self.tricks_won = [[], [], [], []]
        self.score = [0] * 4
        self.player_cb = player_cb
        self.hearts_broken = False
        self.num_rounds = 0


    def deal(self):
        # create deck of cards. J=11, Q=12, K=13, A=14
        deck = [Card(v, s) for v in range(2, 15) for s in ['c', 'd', 'h', 's']]
        # shuffle deck
        random.shuffle(deck)
        # deal out to each player
        self.hands = [deck[:13], deck[13:26], deck[26:39], deck[39:]]


    # passing direction goes in the following order: clockwise, counterclockwise, across, none
    def pass_cards(self, round_num):
        # dont pass on multiples of four
        if round_num % 4 == 0:
            return

        # all players pass cards first
        cards = []
        for p in range(4):
            # get passed cards
            cards.append(self.player_cb(p, self.hands[p]))
            for c in cards[p]:
                self.hands[p].remove(c)

        # then give new cards to players
        for p in range(4):
            # clockwise
            if round_num % 4 == 1:
                self.hands[(p + 1) % 4] += cards[p]
            # counterclockwise
            elif round_num % 4 == 2:
                self.hands[(p - 1) % 4] += cards[p]
            # across
            else:
                self.hands[(p + 2) % 4] += cards[p]


    def trick(self, starting_player):
        # play trick
        trick_cards = []
        for i in range(4):
            trick_cards.append(self.player_cb((starting_player + i) % 4, trick_cards))

        # test if hearts has been broken
        if not self.hearts_broken:
            for c in trick_cards:
                if c.suit == 'h':
                    self.hearts_broken = True

        # find out who won the trick
        winner = 0
        for p in range(1, 4):
            # trump suit
            if trick_cards[p].suit == 's':
                if trick_cards[winner].suit == 's':
                    if trick_cards[p].value > trick_cards[winner].value:
                        winner = p
                # trump suit beats all
                else:
                    winner = p
            # following suit
            elif trick_cards[p].suit == trick_cards[0].suit:
                # trump beats following suit
                if trick_cards[winner].suit != 's':
                    if trick_cards[p].value > trick_cards[winner].value:
                        winner = p

        # winner gets all trick cards
        self.tricks_won[winner] += trick_cards
        return winner


    def update_scores(self):
        round_scores = [0] * 4

        # go through all cards won by each player
        for p in range(4):
            for c in self.tricks_won[p]:
                # add 1 for each heart and 13 for queen of spades
                if c[1] == 'h':
                    round_scores[p] += 1

                elif c == (12, 's'):
                    round_scores[p] += 13

        # a player has shot the moon!
        if round_scores.count(26) != 0:
            moon_shooter = round_scores.index(26)
            decision = self.player_cb(moon_shooter, "You shot the moon! :o")

            # subtract points from own score
            if decision < 0:
                round_scores[moon_shooter] = -26

            # add points to other players scores
            else:
                for i in range(1, 4):
                    round_scores[(moon_shooter + i) % 4] = 26

        # add round scores to game score
        for p in range(4):
            self.scores[p] += round_scores[p]


    def game_over(self):
        if [s >= 100 for s in self.scores].count(True) or self.rounds_played > 20:
            return True
        else:
            return False


    def play(self):
        while not self.game_over():
            self.num_rounds += 1
            # shuffle and deal out deck to each player
            self.deal()
            # players pick 3 cards to pass depending on the round number
            self.pass_cards(self.num_rounds)

            # player with 2 of clubs starts the trick
            starting_player = 0
            while self.hands[starting_player].count((2, 'c')) == 0:
                starting_player = + 1

            # play all 13 tricks
            for _ in range(13):
                starting_player = trick(starting_player)

            # calculate scores
            self.update_scores()

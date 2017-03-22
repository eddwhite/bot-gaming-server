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


class Hearts:
    def __init__(self, player_cb):
        self.hands = []
        self.tricks_won = [ [], [], [], []]
        self.score = [0] * 4
        self.player_cb = player_cb
        self.hearts_broken = False
        self.rounds_played = 0


    def deal(self):
        # create deck of cards. J=11, Q=12, K=13, A=14
        deck = [(v,s) for v in range(2,15) for s in ['c', 'd', 'h', 's']]
        # shuffle deck
        random.shuffle(deck)
        # deal out to each player
        self.hands = [deck[:13], deck[13:26], deck[26:39], deck[39:]]


    def pass_cards(self, direction):
        # all players pass cards first
        cards = []
        for p in range(4):
            # get passed cards
            cards.append(self.player_cb(p, self.hands[p]))
            for c in cards[p]:
                self.hands[p].remove(c)

        # then give new cards to players
        for p in range(4)
            if direction == "cw":
                self.hands[(p+1)%4] += cards[p]
            elif direction == "ccw":
                self.hands[(p-1)%4] += cards[p]
            else:
                self.hands[(p+2)%4] += cards[p]


    def trick(self, starting_player):
        # play trick
        trick_cards = []
        for i in range(4):
            trick_cards.append(self.player_cb((starting_player+i)%4, trick_cards)[0])

        # test if hearts has been broken
        if !self.hearts_broken:
            for c in trick_cards:
                if c[1] == 'h':
                    self.hearts_broken = True

        # find out who won the trick
        winner = 0
        for p in range(1,4):
            # trump suit
            if trick_cards[p][1] == 's':
                if trick_cards[winner][1] == 's':
                    if trick_cards[p][0] > trick_cards[winner][0]:
                        winner = p
                # trump suit beats all
                else:
                    winner = p
            # following suit
            elif trick_cards[p][1] == trick_cards[0][1]:
                # trump beats following suit
                if trick_cards[winner][1] != 's':
                    if trick_cards[p][0] > trick_cards[winner][0]:
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
                self.scores[moon_shooter] -= 26

            # add points to other players scores
            else:
                for i in range(1,4):
                    self.scores[(moon_shooter+i)%4] += 26


    def game_over(self):
        if [s>=100 for s in self.scores].count(True) or self.rounds_played > 20:
            return True
        else:
            return False


    def play(self):
        while !self.game_over():
            # shuffle and deal out deck to each player
            self.deal()
            # players pick 3 cards to pass depending on the round number

            # player with 2 of clubs starts the trick
            starting_player = 0
            while self.hands[starting_player].count((2, 'c')) == 0:
                starting_player =+ 1

            # play all 13 tricks
            for _ in range(13):
                starting_player = trick(starting_player)

            # calculate scores
            self.update_scores()
            self.rounds_played += 1

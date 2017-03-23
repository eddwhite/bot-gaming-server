#!/bin/python3
'''
Goofspiel (the game of pure strategy)
'''

import random


class Goofspiel:
    def __init__(self, player_cb):
        self.player_cb = player_cb
        # Ace (low): 1, J: 11, Q: 12, K: 13
        # track cards played by each player
        self.hands = [list(range(1, 14)) for player in range(2)]
        self.results = []
        self.prizes = list(range(1, 14))
        # randomise order of prize cards
        random.shuffle(self.prizes)


    def players_move(self, player, prize):
        c = self.player_cb(0, prize)
        if self.hands[player].count(c) == 1:
            self.hands[player].remove(c)
        else:
            print("Player {0} is a cheat!".format(player))

        return c


    def play(self):
        for p in self.prizes:
            # get players moves
            m0 = self.players_move(0, p)
            m1 = self.players_move(1, p)

            # sign of score indicates winner
            # player 0: negative, player 1: positive
            if m0 > m1:
                winner = -p
            elif m1 > m0:
                winner = p
            else:
                # draw
                winner = 0

            self.results.append(winner)

        # sum all results of that players sign to get scores
        p0_score = abs(sum(filter(lambda x: x < 0, results)))
        p1_score = abs(sum(filter(lambda x: x > 0, results)))

        # figure out winner
        if p0_score > p1_score:
            print("Player 0 wins")
        elif p1_score > p0_score:
            print("Player 1 wins")
        else:
            # draw
            print("It's a draw")

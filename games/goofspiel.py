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
        self.played = []
        self.prizes = list(range(1, 14))
        # randomise order of prize cards
        random.shuffle(self.prizes)


    def reset(self):
        # Ace (low): 1, J: 11, Q: 12, K: 13
        # track cards played by each player
        self.hands = [list(range(1, 14)) for player in range(2)]
        self.played = []
        # randomise order of prize cards
        random.shuffle(self.prizes)


    def players_move(self, player, prize):
        # send, if available, previous card played by opponent
        info = [prize]
        if self.played != []:
            info.append(self.played[-1][1-player])

        c = self.player_cb(player, info)

        if self.hands[player].count(c) == 1:
            self.hands[player].remove(c)
        else:
            print("Player {0} is a cheat!".format(player))

        return c


    def winner(self):
        # sum all results of that players sign to get scores
        scores = [0, 0]
        for bid in self.played:
            turn = self.played.index(bid)
            # check it wasn't a draw
            if bid.count(max(bid)) == 1:
                scores[bid.index(max(bid))] += self.prizes[turn]
        
        print("Player 1: {0}\tPlayer 2: {1}".format(score[0], score[1]))

        # figure out winner
        if scores.count(max(scores)) == 1:
            print("Player {0} wins".format(scores.index(max(scores))))
        else:
            # draw
            print("It's a draw")
            

    def play(self):
        # reveal prize one by one
        for p in self.prizes:
            # get players moves
            bids = []
            for player in range(2):
                bids.append(self.players_move(player, p))

            self.played.append(bids)

        self.winner()
        

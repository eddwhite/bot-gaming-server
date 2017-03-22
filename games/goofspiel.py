#!/bin/python3
'''
Goofspiel (the game of pure strategy)
'''

import random


class Goofspiel:
    def __init__(self, player_cb):
        self.player_cb = player_cb

    def play():


def play(player_cb):
    # randomise ordrer of "prizes"
    prizes = [i for i in range(1,14)]
    random.shuffle(prizes)
    # track cards played and the score
    p1_hand, p2_hand = [[i for i in range(1,14)] for j in range(2)]
    results = []
    # reveal prizes to players and compare their bids
    for p in prizes:
        m1 = player_cb(1, [p])[0] # get player 1 move

        if p1_hand.count(m1) == 1:
            p1_hand.remove(m1)
        else:
            print("Cheat!")

        m2 = player_cb(2, [p])[0] # get player 2 move

        if p2_hand.count(m2) == 1:
            p2_hand.remove(m2)
        else:
            print("Cheat!")

        # sign of score indicates winner
        # player 1: negative, player 2: positive
        if m1 > m2:
            winner = -p
        elif m1 < m2:
            winner = p
        else:
            winner = 0

        results.append(winner)

    # sum all results of that players sign to get scores
    scores.append(abs(sum(filter(lambda x: x<0, results))))
    scores.append(abs(sum(filter(lambda x: x>0, results))))

    # figure out winner
    if scores[0] > scores[1]:
        # player 1 is winner
        print("Player 1 wins")
    elif scores[0] < scores[1]:
        # player 2 is winner
        print("Player 2 wins")
    else:
        # draw
        print("It's a draw")

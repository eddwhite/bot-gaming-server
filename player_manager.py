#!/bin/python3
'''
Handle communication with players
'''

from games.goofspiel import Goofspiel
from games.hearts import Hearts


def player_cb(player, info):
    print("Player: " + str(player))
    print("Information: " + str(info))
    return input("What card are you playing? ")


def main():
    game_str = input("What game do you want to play?").lower()
    if game_str == "goofspiel":
        game = Goofspiel(player_cb)
    elif game_str == "hearts":
        game = Hearts(player_cb)
    else:
        print("Here is a list of the current games:")
        print("goofspiel")
        print("hearts")
        return False

    game.play()
    return True


if __name__ == "__main__":
    while main():
        print("\nLet's try again... ")

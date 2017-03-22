#!/bin/python3
'''
Handle communication with players
'''

from games import goofspiel
from games import hearts


def player_cb(player, info):
    print("Player: " + str(player))
    print("Information: " + str(info))
    return [int(input("What card are you playing? "))]


def main():
    game = input("What game do you want to play?").lower()
    if game == "goofspiel":
        goofspiel.play(player_cb)
    elif game == "hearts":
        hearts = Hearts(player_cb)
        hearts.play()
    else:
        print("Here is a list of the current games:")
        print("goofspiel")
        print("hearts")
        


if __name__ == "__main__":
    main()

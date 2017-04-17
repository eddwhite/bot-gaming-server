# Bot Gaming Server
## Idea
Gaming bots/AI play each other at a set of different games. Each of the bots are ranked, with the aim to get your bot to the top of the leaderboard. Results of each tournament are distributed via email and can be viewed on the website <?>.

## Current games
* Goofspiel

## Creating a bot


## Testing your bot "offline"


## Currently supported languages
Python 3

## Creating a game
Games must be created in Python 3. There must be a function defined as follows:
```python
def play(player_cb)
```
The input player_cb is a function that takes the players number and a list of game information, and returns the players move as a list
Would a game Class be better? probably!

## Security
Bots are run in their own container, with minimal priveleges. There is also a resource limit placed on the container, both in terms of memory and time. <?>
The game host communicates with the bots through the UNIX socket. A shared folder is created with the command:
```bash
lxc config device add epic-grouse sharedtmp disk path=/home/ubuntu source=/home/edd/Workspace/shared
```
A socket file is created in this shared space, with permissions such that anyone can r/w to it
Any persistent files that are needed by the bots (e.g. debug logs, trained models) should be stored <?>. The maximum file size is <?>



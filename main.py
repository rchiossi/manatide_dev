#!/usr/bin/python3

from manatide.deck import Deck
from manatide.gamestate import GameState
from manatide.player import Player
from manatide.zone import Zone

from util.log import log

def main():
    players = [Player("/home/rchiossi/delver.txt"), Player("/home/rchiossi/delver.txt")]
    print(players)

    state = GameState(players)
    print(state)

if __name__ == '__main__':
    main()

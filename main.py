#!/usr/bin/python3

from manatide.core.deck import Deck
from manatide.core.game import Game
from manatide.core.gameloop import GameLoop
from manatide.core.zone import Zone

from manatide.util.log import log

def main():
    game = Game(2)

    game.set_starting_player(game.players[0].id)

    gameloop = GameLoop(game)

    gameloop.loop()

if __name__ == '__main__':
    main()

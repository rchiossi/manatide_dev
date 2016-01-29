#!/usr/bin/python3

from manatide.core.deck import Deck
from manatide.core.game import Game
from manatide.core.gameloop import GameLoop
from manatide.core.player import ConsolePlayer
from manatide.core.zone import Zone

from manatide.util.log import log

def main():
    players = [ConsolePlayer("test_deck.txt"), ConsolePlayer("test_deck.txt")]

    game = Game(players)

    game.set_starting_player(players[0].id)

    gameloop = GameLoop(game)

    gameloop.loop()

if __name__ == '__main__':
    main()

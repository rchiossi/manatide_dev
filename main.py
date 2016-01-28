#!/usr/bin/python3

from manatide.deck import Deck
from manatide.game import Game
from manatide.gameloop import GameLoop
from manatide.player import ConsolePlayer
from manatide.zone import Zone

from util.log import log

def main():
    players = [ConsolePlayer("test_deck.txt"), ConsolePlayer("test_Deck.txt")]

    game = Game(players)

    game.set_starting_player(players[0].id)

    gameloop = GameLoop(game)

    gameloop.loop()

if __name__ == '__main__':
    main()

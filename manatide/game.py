import random
import uuid

from enum import Enum

from manatide.objects import Card
from manatide.zone import Zone

from util.log import log

class GameState(Enum):
    RUNNING = 0
    TERMINATED = 1

class Game(object):
    def __init__(self, players):
        if players is None or len(players) == 0:
            log.e("Invalid players list")

        self.id = uuid.uuid4()

        self.state = GameState.RUNNING

        self.objects = []
        #TODO: Load rules
        self.rules = []

        self.players = players
        self.active_player = None

        self.current_player = None

        self.zones = {
                "battlefield": Zone("battlefield"),
                "stack": Zone("stack"),
                "exile": Zone("exile"),
                "ante": Zone("ante"),
                "command": Zone("command")
                }

        for player in players:
            library = Zone("library")

            for card_name, amount in player.deck.main.items():
                for i in range(int(amount)):
                    #load card
                    #card = Card(card_name)
                    #card.load(library, player)
                    pass

            library.exhausted = False

            self.zones["library", player.id] = library
            self.zones["hand", player.id] = Zone("hand")
            self.zones["graveyard", player.id] = Zone("graveyard")

    def set_starting_player(self, pid):
        for player in self.players:
            if player.id is not pid:
                continue

            self.current_player = player
            self.active_player = player

    def __str__(self):
        return "Game[{}]".format(self.id)

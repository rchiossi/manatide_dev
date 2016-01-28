import collections
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

        self.players = collections.deque(players)
        self.active_player = None

        self.manapool = {
                "black": 0,
                "blue": 0,
                "gree": 0,
                "red": 0,
                "white": 0,
                "colorless": 0,
                }

        self.zones = {
                "battlefield": Zone("battlefield"),
                "stack": Zone("stack"),
                "exile": Zone("exile"),
                "ante": Zone("ante"),
                "command": Zone("command")
                }

        for player in players:
            library = Zone("library")
            library.exhausted = False

            self.zones["library", player.id] = library
            self.zones["hand", player.id] = Zone("hand")
            self.zones["graveyard", player.id] = Zone("graveyard")

    def set_starting_player(self, pid):
        while self.players[0].id is not pid:
            self.players.rotate(1)

        self.active_player = self.players[0]

    def __str__(self):
        return "Game[{}]".format(self.id)

import collections
import random
import uuid

from enum import Enum

from manatide.core.event import EventQueue
from manatide.core.objects import Card
from manatide.core.player import ConsolePlayer
from manatide.core.turn import Turn
from manatide.core.zone import Zone

from manatide.rules import RulePriorityPass
from manatide.rules import RuleAdvanceTurn

from manatide.util.log import log

class GameState(Enum):
    RUNNING = 0
    TERMINATED = 1

class Game(object):
    def __init__(self, num_players):
        if num_players < 2:
            log.e("Invalid number of players")

        self.id = uuid.uuid4()

        self.state = GameState.RUNNING

        self.objects = []
        #TODO: Load rules
        self.rules = [RulePriorityPass(), RuleAdvanceTurn()]

        #TODO: Allow different types of players
        self.players = collections.deque()
        for i in range(num_players):
            self.players.append(ConsolePlayer(self))

        self.active_player = None

        self.event_queue = EventQueue(self)
        self.event_history = []

        self.turn = Turn(self)

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

        for player in self.players:
            library = Zone("library")
            library.exhausted = False

            self.zones["library", player.id] = library
            self.zones["hand", player.id] = Zone("hand")
            self.zones["graveyard", player.id] = Zone("graveyard")

            #TODO: handle deck loading
            player.load_deck()
            for card in player.deck.main:
                card.load(library, player)
                library.add_object(card)
                self.objects.append(card)

    def set_starting_player(self, pid):
        while self.players[0].id is not pid:
            self.players.rotate(1)

        self.active_player = self.players[0]

    def queue(self, event, priority=False):
        self.event_queue.queue(event, priority)

    def __str__(self):
        return "Game[{}]".format(self.id)

import random
import uuid

from manatide.card import Card
from manatide.zone import Zone

from util.log import log

class Game(object):
    def __init__(self, players):
        if players is None or len(players) == 0:
            log.e("Invalid players list")

        self.id = uuid.uuid4()

        self.objects = []
        #TODO: Load rules
        self.rules = []

        self.players = players
        self.active_player = None

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
                    card = Card(card_name)
                    card.load(library, player)

            library.exhausted = False

            self.zones["library", player.id] = library
            self.zones["hand", player.id] = Zone("hand")
            self.zones["graveyard", player.id] = Zone("graveyard")

    def __str__(self):
        return "Game[{}]".format(self.id)

from manatide.core.event import EventStatus
from manatide.core.objects import Card
from manatide.core.types import SuperTypes
from manatide.core.types import Types
from manatide.core.types import LandTypes

from manatide.events import EventManaAdd
from manatide.events import EventTap

class Island(Card):
    def load(self):
        self.name = "Island"

        self.supertype = [SuperTypes.BASIC]
        self.type = [Types.LAND]
        self.subtype = [LandTypes.ISLAND]

        self.activated_abilities = [self.tap_for_mana]

    def tap_for_mana(self, game):
        linked_event = EventManaAdd(self.controller, EventStatus.OK, "blue")
        event = EventTap(self.controller, None, self, linked_event)

        game.event_queue.queue(event)


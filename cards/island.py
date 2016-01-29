from manatide.core.objects import Card
from manatide.core.types import SuperTypes
from manatide.core.types import Types
from manatide.core.types import LandTypes

from manatide.events import EventManaAdd
from manatide.events import EventTap

class Island(Card):
    name = "Island"

    supertype = [SuperTypes.BASIC]
    type = [Types.LAND]
    subtype = [LandTypes.ISLAND]

    def ability(self, game):
        linked_event = EventManaAdd("blue")
        event = EventTap(self, linked_event)

        game.event_queue.queue(event)

    activated_abilities = [ability]


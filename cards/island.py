from manatide.objects import Card
from manatide.types import SuperTypes
from manatide.types import Types
from manatide.types import LandTypes

class Island(Card):
    name = "Island"

    supertype = [SuperTypes.BASIC]
    type = [Types.LAND]
    subtype = [LandTypes.ISLAND]

    def ability(self, game):
        linked_event = EventAddMana("blue")
        event = EventTap(self, linked_event)

        game.event_queue.queue(event)

    activated_abilities = [ability]


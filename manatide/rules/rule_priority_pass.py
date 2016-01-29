from manatide.core.event import EventStatus
from manatide.core.rule import Rule
from manatide.events import EventPriorityPass

class RulePriorityPass(Rule):
    target_event = EventPriorityPass

    def prepare(self, event, game):
        if event.player is game.players[0]:
            event.status = EventStatus.OK
        else:
            event.status = EventStatus.ABORTED


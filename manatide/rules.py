import uuid

from manatide.events import EventStatus
from manatide.events import EventPriorityPass

from util.log import log

class Rule(object):
    event_type = None

    prepare = None
    resolve = None
    done = None

    def __init__(self):
        self.id = uuid.uuid4()

    def filter(self, event, game):
        log.d("filter(): {}".format(self))
        return True

    def apply(self, event):
        log.d("apply(): {}".format(self))

        if self.prepare is not None:
            event.rules["prepare"].append(self)

        if self.resolve is not None:
            event.rules["resolve"].append(self)

        if self.done is not None:
            event.rules["done"].append(self)

    def __str__(self):
        return "{}[{}]".format(self.__class__.__name__, self.id.hex[:8])

class RulePriorityPass(Rule):
    event_type = EventPriorityPass

    def prepare(self, event, game):
        log.d("prepare(): {}".format(self))
        if event.player is game.players[0]:
            event.status = EventStatus.OK
        else:
            event.status = EventStatus.ABORTED


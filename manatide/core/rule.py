import uuid

from manatide.core.event import EventStatus
from manatide.events.event_priority_pass import EventPriorityPass

from manatide.util.log import log

class Rule(object):
    target_event = None

    prepare = None
    resolve = None
    done = None

    def __init__(self):
        self.id = uuid.uuid4()

    def filter(self, event, game):
        return True

    def check_filter(self, event, game):
        log.d("check_filter(): {}".format(self))

        if event.__class__ is not self.target_event:
            return False

        return self.filter(event, game)

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


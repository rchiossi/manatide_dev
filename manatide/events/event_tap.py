from manatide.core.event import Event
from manatide.util.log import log

class EventTap(Event):
    def __init__(self, player, objs, linked_event=None):
        if objs is None:
            log.e("No object for event {}".format(self))

        self.objs = objs
        self.linked_event = linked_event

    def resolve(self, game):
        for obj in self.objs:
            obj.tapped = True

        if self.linked_event is not None:
            game.event_queue.queue(linked_event)


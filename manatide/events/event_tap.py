from manatide.core.event import Event
from manatide.util.log import log

class EventTap(Event):
    def load(self, player, status, objs, linked_event=None):
        if objs is None:
            log.e("No object for event {}".format(self))

        self.player = player
        self.objs = objs
        self.linked_event = linked_event

    def resolve(self):
        for obj in self.objs:
            obj.tapped = True

        if self.linked_event is not None:
            self.queue(linked_event)


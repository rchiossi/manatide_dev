from manatide.core.event import Event
from manatide.util.log import log

class EventTransition(Event):
    def load(self, player, status, objs, zone):
        if objs is None:
            log.e("No object for event {}".format(self))

        if zone is None:
            log.e("No zone for event {}".format(self))

        self.objs = objs
        self.zone = zone

    def prepare(self, game):
        for obj in self.objs:
            self.zone.stage_obj(obj)

    def resolve(self, name):
        self.zone.commit_staged()


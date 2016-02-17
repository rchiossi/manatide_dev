from manatide.core.event import Event
from manatide.core.event import EventStatus
from manatide.util.log import log

class EventTransition(Event):
    def load(self, game, player, status, objs, zone_name):
        if objs is None:
            log.e("No object for event {}".format(self))

        if zone_name is None:
            log.e("No zone for event {}".format(self))

        self.objs = objs
        self.zone_name = zone_name
        self.zones = []

    def prepare(self):
        for obj in self.objs:
            zone = self.game.zones[self.zone_name, obj.owner.id]

            if zone not in self.zones:
                self.zones.append(zone)

            zone.stage_obj(obj)

    def resolve(self):
        for zone in self.zones:
            zone.commit_staged()

class EventDraw(Event):
    def resolve(self):
        library = self.game.zones["library", self.player.id]

        if len(library.objects) == 0:
            library.exhausted = True
            return

        objs = [library.objects[-1]]
        self.game.queue(EventTransition(self.game, self.player, EventStatus.OK, objs, "hand"), True)




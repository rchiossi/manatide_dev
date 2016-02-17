from manatide.core.event import Event
from manatide.core.event import EventStatus

from manatide.events import EventDraw

class EventBeginningPhase(Event):
    def resolve(self):
        self.game.queue(EventUntapStep(self.game, status=EventStatus.OK), True);


class EventUntapStep(Event):
    def resolve(self):
        #TODO: Handle Phasing

        for card in self.game.zones["battlefield"]:
            if card.controller is game.active_player:
                self.game.queue(EventUntap(self.game, objs=[card]))

        self.game.turn.advance()


class EventUpkeepStep(Event):
    pass


class EventDrawStep(Event):
    def resolve(self):
        self.game.queue(EventDraw(self.game, self.game.active_player, EventStatus.OK))


class EventMainPhase(Event):
    pass


class EventCombatPhase(Event):
    def resolve(self):
        self.game.queue(EventBeginningOfCombatStep(self.game, status=EventStatus.OK), True);


class EventBeginningOfCombatStep(Event):
    pass


class EventDeclareAttackersStep(Event):
    pass


class EventDeclareBlockersStep(Event):
    pass


class EventCombatDamageStep(Event):
    pass


class EventEndOfCombatStep(Event):
    pass


class EventEndPhase(Event):
    def resolve(self):
        self.game.queue(EventEndStep(), True);


class EventEndStep(Event):
    pass


class EventCleanupStep(Event):
    pass



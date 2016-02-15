from manatide.core.event import Event
from manatide.core.event import EventStatus

class EventBeginningPhase(Event):
    def resolve(self, game):
        game.queue(EventUntapStep(), True);


class EventUntapStep(Event):
    def load(self, playeri, status):
        self.status = EventStatus.OK

    def resolve(self, game):
        #TODO: Handle Phasing

        for card in game.zones["battlefield"]:
            if card.controller is game.active_player:
                game.queue(EventUntap(card))

        game.turn.advance()


class EventUpkeepStep(Event):
    pass


class EventDrawStep(Event):
    pass


class EventMainPhase(Event):
    pass


class EventCombatPhase(Event):
    def resolve(self, game):
        game.queue(EventBeginningOfCombatStep(), True);


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
    def resolve(self, game):
        game.queue(EventEndStep(), True);


class EventEndStep(Event):
    pass


class EventCleanupStep(Event):
    pass



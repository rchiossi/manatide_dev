from manatide.core.event import Event

class EventPriorityPass(Event):
    def resolve(self, game):
        game.players.rotate(1)

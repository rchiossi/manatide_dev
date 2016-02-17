from manatide.core.event import Event

class EventPriorityPass(Event):
    def resolve(self):
        self.game.players.rotate(1)

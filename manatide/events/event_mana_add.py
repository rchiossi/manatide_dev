from manatide.core.event import Event

class EventManaAdd(Event):
    def load(self, playeri, status, color, amount=1):
        self.color = color
        self.amount = amount

    def resolve(self, game):
        game.manapool[self.color] += self.amount


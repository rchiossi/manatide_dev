from manatide.core.event import Event

class EventManaAdd(Event):
    def load(self, game, player, status, color, amount=1):
        self.color = color
        self.amount = amount

    def resolve(self):
        self.game.manapool[self.color] += self.amount


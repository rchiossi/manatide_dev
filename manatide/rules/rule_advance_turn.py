from manatide.core.rule import Rule
from manatide.events import EventPriorityPass

class RuleAdvanceTurn(Rule):
    def load(self):
        self.target_event = EventPriorityPass

    def done(self, event, game):
        if len(game.event_history) > 0 and game.event_history[-1] == EventPriorityPass:
            game.turn.advance()


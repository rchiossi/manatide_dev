from manatide.core.rule import Rule
from manatide.events import EventPriorityPass

class RuleAdvanceTurn(Rule):
    def load(self):
        self.target_event = EventPriorityPass

    def done(self, event, game):
        if len(game.event_history) < len(game.players) - 1:
            return

        for i in range(1, len(game.players)):
            if game.event_history[-i] != EventPriorityPass:
                return

        game.turn.advance()


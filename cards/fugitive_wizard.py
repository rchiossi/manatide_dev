from manatide.core.objects import Card
from manatide.core.types import Types
from manatide.core.types import CreatureTypes

class FugitiveWizard(Card):
    def load(self):
        self.name = "Fugitive Wizard"

        self.manacost = "{U}"

        self.type = [Types.CREATURE]
        self.subtype = [CreatureTypes.HUMAN, CreatureTypes.WIZARD]

        self.power = 1
        self.toughness = 1


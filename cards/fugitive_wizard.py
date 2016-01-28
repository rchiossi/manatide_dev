from manatide.objects import Card
from manatide.types import Types
from manatide.types import CreatureTypes

class FugitiveWizard(Card):
    name = "Fugitive Wizard"

    type = [Types.CREATURE]
    subtype = [CreatureTypes.HUMAN, CreatureTypes.WIZARD]

    power = 1
    toughness = 1


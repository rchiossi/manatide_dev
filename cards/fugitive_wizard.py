from manatide.core.objects import Card
from manatide.core.types import Types
from manatide.core.types import CreatureTypes

class FugitiveWizard(Card):
    name = "Fugitive Wizard"

    type = [Types.CREATURE]
    subtype = [CreatureTypes.HUMAN, CreatureTypes.WIZARD]

    power = 1
    toughness = 1


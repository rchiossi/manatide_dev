import uuid

from manatide.util.log import log

class GenericObject(object):
    def __init__(self):
        self.id = None
        self.id_history = []

        self.name = None
        self.zone = None
        self.previous_zone = None
        self.owner = None
        self.controller = None

        self.update_id()

    def update_id(self):
        self.id = uuid.uuid4()
        self.id_history.append(self.id)

    def load(self, zone, owner, controller=None):
        self.update_id()

        self.zone = zone
        self.owner = owner
        self.controller = controller

    def __str__(self):
        return "GenericObject[{}:{}]".format(self.name, self.id.hex[:8])

class Card(GenericObject):
    def __init__(self):
        super().__init__()

        self.name = None
        self.manacost = None
        self.supertype = []
        self.type = []
        self.subtype = []
        self.color_indicator = []
        self.text = ""
        self.power = None
        self.toughness = None
        self.loyalty = None

        self.activated_abilities = []
        self.static_abilities = []

        self.tapped = False
        self.flipped = False
        self.facedown = False
        self.phaseout = False

        self.load()

    def load(self):
        pass

    def __str__(self):
        return "Card[{}:{}]".format(self.name, self.id.hex[:8])


class Ability(GenericObject):
    def __init__(self):
        self.description()

    def __str__(self):
        return "Ability[{}:{}]".format(self.name, self.id.hex[:8])

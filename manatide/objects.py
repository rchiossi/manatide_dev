import uuid

from util.log import log

class GenericObject(object):
    name = None

    def __init__(self):
        self.id = None
        self.id_history = []

        self.zone = None
        self.previous_zone = None
        self.owner = None
        self.controller = None

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
    supertype = []
    type = []
    subtype = []
    activated_abilities = []

    def __init__(self):
        super().__init__()

        self.tapped = False
        self.flipped = False
        self.facedown = False
        self.phaseout = False

    def __str__(self):
        return "Card[{}:{}]".format(self.name, self.id.hex[:8])


class Ability(GenericObject):
    def __init__(self):
        self.description()

    def __str__(self):
        return "Ability[{}:{}]".format(self.name, self.id.hex[:8])
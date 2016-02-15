import uuid

from enum import Enum

from manatide.util.log import log

class Zone(object):
    def __init__(self, name):
        if name is None:
            log.e("Invalid name for Zone")

        self.id = uuid.uuid4()

        self.name = name

        self.objects = []
        self.staged = []

    def stage_obj(self, card):
        self.staged.append(card)

    def commit_staged(self):
        for obj in staged:
            obj.previous_zone = obj.zone
            obj.previous_zone.remove_object(obj)
            obj.zone = self

            obj.update_id()

        self.objects.append(self.staged)

        committed = self.staged
        self.staged = []

        return committed

    def add_object(self, card):
        if card is None:
            log.e("Null card added to zone {}".format(zone.name))

        self.objects.append(card)

    def remove_object(self, card):
        if card is None:
            log.e("Null card removed to zone {}".format(zone.name))

        self.objects.remove(card)

    def __iter__(self):
        return self.objects.__iter__()

    def __str__(self):
        return "Zone[{}]".format(self.name)


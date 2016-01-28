from enum import Enum

from util.log import log

class EventStatus(Enum):
    ABORTED = 0
    OK = 1
    UNVERIFIED = 2


class EventQueue(object):
    def __init__(self, game):
        self.event_queue = []

        self.game = game

    def queue(self, event):
        self.event_queue.insert(0, event)

    def queue_priority(self, event):
        self.event_queue.append(event)

    def step(self):
        if len(self.event_queue) is 0:
            return None

        event = self.event_queue.pop()

        log.i("EventQueue: {}".format(event))

        for obj in game.objects:
            if event.hook in obj.__dict__.keys():
                getattr(obj, event.hook)(event)

        getattr(game.rules, event.hook)(event)

        return event.process(self.game)


class Event(object):
    hook = None

    def __init__(self, player):
        self.status = EventStatus.UNVERIFIED

        self.player = player

        hooks = {"pre": [], "ongoing": [], "post": []}

    def process(self, game):
        log.e("process() not implemented for class {}".format(self))

    def process_hooks(self, game, hook_name):
        for hook in hooks[hook_name]:
            status = hook(game, self)

            if status is EventStatus.UNVERIFIED:
                continue

            self.status = status

            if status is EventStatus.ABORTED:
                return False

        return self.status is EventStatus.OK 

    def __str__(self):
        return self.__class__.__name__


class EventTransition(Event):
    hook = "hook_transition"

    def __init__(self, player, objs, zone):
        super().__init__(player)

        if objs is None:
            log.e("No object for event {}".format(self))

        if zone is None:
            log.e("No zone for event {}".format(self))

        self.objs = objs
        self.zone = zone

    def process(self, game):
        if not self.process_hooks(game, "pre"):
            return self.status

        for obj in self.objs:
            self.zone.stage_obj(obj)

        if not self.process_hooks(game, "ongoing"):
            return self.status

        self.zone.commit_staged()

        return self.process_hooks(game, "post")


class EventTap(Event):
    hook = "hook_tap"

    def __init__(self, player, objs, linked_event=None):
        if objs is None:
            log.e("No object for event {}".format(self))

        self.objs = objs
        self.linked_event = linked_event

    def process(self, game):
        if not self.process_hooks(game, "pre"):
            return self.status

        if not self.process_hooks(game, "ongoing"):
            return self.status

        for obj in self.objs:
            obj.tapped = True

        if self.linked_event is not None:
            game.event_queue.queue(linked_event)

        return self.process_hooks(game, "post")


class EventAddMana(Event):
    hook = "hook_add_mana"

    def __init__(self, player, color, amount=1):
        self.color = color
        self.amount = amount 

    def process(self, game):
        if not self.process_hooks(game, "pre"):
            return self.status

        if not self.process_hooks(game, "ongoing"):
            return self.status

        game.manapool[self.color] += self.amount

        return self.process_hooks(game, "post")



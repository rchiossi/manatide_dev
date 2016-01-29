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

    def queue(self, event, priority=False):
        if event is None:
            log.w("NULL event queued")
            return

        for rule in self.game.rules:
            if rule.filter(event, self.game):
                rule.apply(event)

        if priority:
            self.event_queue.append(event)
        else:
            self.event_queue.insert(0, event)

    def step(self):
        if len(self.event_queue) is 0:
            return None

        event = self.event_queue.pop()

        log.i("EventQueue: {}".format(event))

        status = event.process(self.game)

        log.d("EventQueue: {} - {}".format(event, status))

        return status


class Event(object):
    def __init__(self, player):
        self.status = EventStatus.UNVERIFIED
        self.player = player
        self.rules = {"prepare": [], "resolve": [], "done": []}

    def process_rules(self, game, stage):
        for rule in self.rules[stage]:
            getattr(rule, stage)(self, game)

            if self.status is EventStatus.ABORTED:
                return

    def prepare(self, game):
        pass

    def resolve(self, game):
        pass

    def process(self, game):
        for rule in self.rules["prepare"]:
            rule.prepare(self, game)

            if self.status is EventStatus.ABORTED:
                break

        if self.status is not EventStatus.OK:
            return self.status

        self.prepare(game)

        for rule in self.rules["resolve"]:
            rule.resolve(self, game)

            if self.status is EventStatus.ABORTED:
                break

        if self.status is not EventStatus.OK:
            return self.status

        self.resolve(game)

        for rule in self.rules["done"]:
            rule.done(self, game)

        return self.status

    def __str__(self):
        return self.__class__.__name__


class EventTransition(Event):
    def __init__(self, player, objs, zone):
        super().__init__(player)

        if objs is None:
            log.e("No object for event {}".format(self))

        if zone is None:
            log.e("No zone for event {}".format(self))

        self.objs = objs
        self.zone = zone

    def prepare(self, game):
        for obj in self.objs:
            self.zone.stage_obj(obj)

    def resolve(self, name):
        self.zone.commit_staged()


class EventTap(Event):
    def __init__(self, player, objs, linked_event=None):
        if objs is None:
            log.e("No object for event {}".format(self))

        self.objs = objs
        self.linked_event = linked_event

    def resolve(self, game):
        for obj in self.objs:
            obj.tapped = True

        if self.linked_event is not None:
            game.event_queue.queue(linked_event)


class EventAddMana(Event):
    def __init__(self, player, color, amount=1):
        self.color = color
        self.amount = amount

    def resolve(self, game):
        game.manapool[self.color] += self.amount


class EventPriorityPass(Event):
    def resolve(self, game):
        game.players.rotate(1)



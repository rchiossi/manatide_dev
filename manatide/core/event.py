from enum import Enum

from manatide.util.log import log

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

        if Event not in event.__class__.__bases__:
            log.w("Cannot queue {} as it is a class, not an object. Missing ()?".format(event))
            return

        log.d("Queueing event: {}".format(event))

        for rule in self.game.rules:
            if rule.check_filter(event, self.game):
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

        if status is EventStatus.OK:
            self.game.event_history.append(event)

        return status


class Event(object):
    def __init__(self, player=None, status=None, *args):
        self.rules = {"prepare": [], "resolve": [], "done": []}
        self.player = player

        if status is None:
            self.status = EventStatus.UNVERIFIED
        else:
            self.status = status

        self.load(player, status, *args)

    def load(self, player, *args):
        pass

    def prepare(self, game):
        pass

    def resolve(self, game):
        pass

    def process(self, game):
        for rule in self.rules["prepare"]:
            rule.prepare(self, game)

            if self.status is EventStatus.ABORTED:
                log.d("{} aborted on prepare by rule {}".format(self, rule))
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

    def __eq__(self, event_type):
        return self.__class__ is event_type

    def __str__(self):
        return self.__class__.__name__


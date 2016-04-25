from enum import Enum

from manatide.util.log import log

class EventStatus(Enum):
    OK = 0
    ABORTED = 1
    UNVERIFIED = 2
    WAITING = 3
    DONE = 4


class EventQueueStatus(Enum):
    IDLE = 0
    BUSY = 1
    WAITING = 2


class EventQueue(object):
    def __init__(self, game):
        self.event_queue = []
        self.status = EventQueueStatus.IDLE

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

        if self.status == EventQueueStatus.IDLE:
            self.status = EventQueueStatus.BUSY

    def step(self):
        if self.status == EventQueueStatus.IDLE:
            return

        elif self.status == EventQueueStatus.BUSY:
            if self.process_event() is None:
                self.status = EventQueueStatus.IDLE

        elif self.status == EventQueueStatus.WAITING:
            pass

    def process_event(self):
        if len(self.event_queue) is 0:
            return None

        event = self.event_queue[-1]

        log.i("EventQueue: {}".format(event))

        status = event.process(self.game)

        log.d("EventQueue: {} - {}".format(event, status))

        if status is not EventStatus.WAITING:
            self.event_queue.remove(event)

            if status is EventStatus.DONE:
                self.game.event_history.append(event)

        return status


class Event(object):
    def __init__(self, game, player=None, status=None, *args, **kargs):
        self.rules = {"prepare": [], "resolve": [], "done": []}

        self.game = game
        self.player = player

        self.wait_list = []

        if status is None:
            self.status = EventStatus.UNVERIFIED
        else:
            self.status = status

        self.load(game, player, status, *args, **kargs)

    def load(self, player, *args):
        pass

    def prepare(self):
        pass

    def resolve(self):
        pass

    def should_wait(self):
        for event in self.wait_list:
            if event.status is EventStatus.ABORTED:
                self.status = EventStatus.ABORTED
                return False
            elif event.status is not DONE:
                return True

        return False

    def queue(self, event, priority=False):
        self.game.event_queue.queue(event, priority)

    def wait_on(self, event, priority=False):
        if event is None:
            log.e("Cannot wait on NULL event")

        if event == self:
            log.e("An event cannot wait on itself")

        if self.status is EventStatus.ABORTED:
            log.e("Cannot wait od aborted event")

        self.wait_list.append(event)
        self.game.event_queue.queue(event, priority)

        self.status = EventStatus.WAITING

    def process(self, game):
        if self.status is not EventStatus.WAITING:
            for rule in self.rules["prepare"]:
                rule.prepare(self, game)

                if self.status is EventStatus.ABORTED:
                    log.d("{} aborted on prepare by rule {}".format(self, rule))
                    break

            if self.status is not EventStatus.OK:
                return self.status

            self.prepare()

        self.should_wait()
        if self.status is not EventStatus.OK:
            return self.status

        for rule in self.rules["resolve"]:
            rule.resolve(self, game)

            if self.status is EventStatus.ABORTED:
                break

        if self.status is not EventStatus.OK:
            return self.status

        self.resolve()

        for rule in self.rules["done"]:
            rule.done(self, game)

        self.status = EventStatus.DONE;

        return self.status

    def __eq__(self, event_type):
        return self.__class__ is event_type

    def __str__(self):
        return self.__class__.__name__


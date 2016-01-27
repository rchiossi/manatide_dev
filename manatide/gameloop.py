from enum import Enum

from manatide.event import EventStatus
from util.log import log

class GameLoop(object):
    def __init__(self, game):
        event_queue =

        self.game = game

    def queue_event(self, event):
        event_queue.insert(0, event)

    def queue_event_priority(self, event):
        event_queue.append(event)

    def loop(self):
        if len(event_queue) is 0:
            return False

        event = event_queue.pop()

        if event.handler not in self.__dict__.keys():
            log.w("Invalid event type: {}".format(event.handler))
            return False

        return getattr(self, event.handler)(event)

    def on_event(self, event):
        for obj in game.objects:
            if event.handler in obj.__dict__.keys():
                getattr(obj, event.handler)(event)

    def check_rules(self, event):
        for obj in game.rules:
            if event.handler in obj.__dict__.keys():
                getattr(obj, event.handler)(event)

    def transition_stage(self, event):
        self.on_event(event)

        if event.status is EventStatus.UNVERIFIED:
            self.check_rules(self, event)

        if event.status is EventStatus.OK:
            event.zone.stage_obj(event.obj)

        return event.status is EventStatus.OK

    def transition_ready(self, event):
        self.on_event(event)

        committed = event.zone.commit_staged()

        for obj in committed:
            new_event = EventTransitionCommit(event.player, event.obj, event.zone)
            self.queue_event_priority(new_event)

        return True

    def transition_commit(self, event):
        self.on_event(event)

        return True


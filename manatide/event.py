from enum import Enum

class EventStatus(Enum):
    ABORTED = 0
    OK = 1
    UNVERIFIED = 2

class Event(object):
    handler = None

    def __init__(self, player):
        self.status = EventStatus.UNVERIFIED

        self.player = player

class EventTransition(Event):
    def __init__(self, player, obj, zone):
        super().__init__(player)

        self.obj = obj
        self.zone = zone

class EventTransitionStage(EventTransition):
    handler = 'transition_stage'

class EventTransitionReady(EventTransition):
    handler = 'transition_ready'

class EventTransitionCommit(EventTransition):
    handler = 'transition_commit'


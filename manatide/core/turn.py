from enum import Enum

from manatide.core.event import EventStatus;

from manatide.events import EventBeginningPhase;
from manatide.events import EventUpkeepStep;
from manatide.events import EventDrawStep;
from manatide.events import EventMainPhase;
from manatide.events import EventCombatPhase;
from manatide.events import EventDeclareAttackersStep;
from manatide.events import EventDeclareBlockersStep;
from manatide.events import EventCombatDamageStep;
from manatide.events import EventEndOfCombatStep;
from manatide.events import EventEndPhase;
from manatide.events import EventCleanupStep;

from manatide.util.log import log

class TurnPhase(Enum):
    BEGINNING = 0
    MAIN = 1
    COMBAT = 2
    ENDING = 3


class TurnStep(Enum):
    UNTAP = 0
    UPKEEP = 1
    DRAW = 2
    FIRST_MAIN = 3
    BEGINNING_OF_COMBAT = 4
    DECLARE_ATTACKERS = 5
    DECLARE_BLOCKERS = 6
    COMBAT_DAMAGE = 7
    END_OF_COMBAT = 8
    SECOND_MAIN = 9
    END_STEP = 10
    CLEANUP = 11


class Turn(object):
    def __init__(self, game):
        self.game = game

        self.phase = None
        self.step = None

    def reset(self):
        self.phase = None
        self.step = None

    def advance(self):
        if self.step is None:
            log.d("Turn: Advance to UNTAP STEP")

            self.phase = TurnPhase.BEGINNING
            self.step = TurnStep.UNTAP

            self.game.queue(EventBeginningPhase(status=EventStatus.OK))

        elif self.step is TurnStep.UNTAP:
            log.d("Turn: Advance to UPKEEP STEP")

            self.step = TurnStep.UPKEEP

            self.game.queue(EventUpkeepStep(status=EventStatus.OK), True)

        elif self.step is TurnStep.UPKEEP:
            log.d("Turn: Advance to DRAW STEP")

            self.step = TurnStep.DRAW

            self.game.queue(EventDrawStep(status=EventStatus.OK))

        elif self.step is TurnStep.DRAW:
            log.d("Turn: Advance to FIRST MAIN PHASE")

            self.phase = TurnPhase.MAIN
            self.step = TurnStep.FIRST_MAIN

            self.game.queue(EventMainPhase(status=EventStatus.OK))

        elif self.step is TurnStep.FIRST_MAIN:
            log.d("Turn: Advance to COMBAT PHASE")

            self.phase = TurnPhase.COMBAT
            self.step = TurnStep.BEGINNING_OF_COMBAT

            self.game.queue(EventCombatPhase(status=EventStatus.OK))





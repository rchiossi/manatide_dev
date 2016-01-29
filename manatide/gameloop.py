from enum import Enum

from manatide.events import EventQueue
from manatide.events import EventStatus

from manatide.events import EventPriorityPass

from manatide.game import GameState

from util.log import log

class GameLoop(object):
    def __init__(self, game):
        if game is None:
            log.e("NULL game provided to GameLoop")

        self.game = game

        self.event_queue = EventQueue(game)

    def loop(self):
        while self.game.state is not GameState.TERMINATED:

            while self.event_queue.step() is not None:
                continue

            self.game.players[0].write("Waiting for input")
            cmd = self.game.players[0].read()

            print("echo: {}".format(cmd))

            if 'exit' in cmd:
                self.game.state = GameState.TERMINATED
            elif 'pass' in cmd:
                self.event_queue.queue(EventPriorityPass(self.game.players[0]))

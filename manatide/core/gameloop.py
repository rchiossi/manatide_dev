from enum import Enum

from manatide.core.event import EventStatus
from manatide.core.game import GameState

from manatide.events import EventPriorityPass

from manatide.util.log import log

class GameLoop(object):
    def __init__(self, game):
        if game is None:
            log.e("NULL game provided to GameLoop")

        self.game = game

    def loop(self):
        while self.game.state is not GameState.TERMINATED:

            while self.game.event_queue.step() is not None:
                continue

            self.game.players[0].write("Waiting for input")
            cmd = self.game.players[0].read()

            print("echo: {}".format(cmd))

            tokens = cmd.split(" ")

            self.handle_cmd(tokens[0], tokens[1:])

    def handle_cmd(self, cmd, args):
        if cmd == 'exit' or cmd == 'quit' or cmd == 'q':
            self.game.state = GameState.TERMINATED
        elif cmd == 'pass' or cmd == 'p':
            self.game.queue(EventPriorityPass(self.game, self.game.players[0]))
        elif cmd == 'info' or cmd == 'i':
            if args[0] == "library":
                zone = self.game.zones["library", self.game.active_player.id]
            elif args[0] == "hand":
                zone = self.game.zones["hand", self.game.active_player.id]

            print(zone)
            for obj in zone.objects:
                print(obj)


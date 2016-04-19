from enum import Enum

from manatide.core.event import EventStatus
from manatide.core.event import EventQueueStatus
from manatide.core.game import GameState

from manatide.events import EventPriorityPass

from manatide.util.log import log

class GameLoop(object):
    def __init__(self, game):
        if game is None:
            log.e("NULL game provided to GameLoop")

        self.game = game

    def loop(self):
        self.game.turn.advance()

        while self.game.state is not GameState.TERMINATED:
            self.game.event_queue.step()

            for player in self.game.players:
                cmd = player.read()

                if cmd == None:
                    continue

                tokens = cmd.split(" ")
                self.cmd_handler(player, tokens[0], tokens[1:])

    def cmd_handler(self, player, cmd, args):
        if cmd == 'exit' or cmd == 'quit' or cmd == 'q':
            self.game.state = GameState.TERMINATED
        elif cmd == 'pass' or cmd == 'p':
            self.game.queue(EventPriorityPass(self.game, self.game.players[0]))
        elif cmd == 'info' or cmd == 'i':
            self.handle_info(player, args)
        elif cmd == 'cast' or cmd == 'c':
            self.handle_cast(player, args)
        else:
            player.write("Invalid command: '{}'".format(cmd))

    def find_player(self, player_id):
        for player in self.game.players:
            if player.id.hex.startswith(player_id):
                return player
        return None

    def find_object(self, obj_id):
        for obj in self.game.objects:
            if obj.id.hex.startswith(obj_id):
                return obj
        return None

    def print_zone(self, player, zone_name, args=None):
        if args is not None and len(args) > 0:
            target_player = self.find_player(args[0])

            if target_player is None:
                player.write("Player '{}' not found".format(args[1]))
                return
        elif args is not None:
            target_player = player
        else:
            target_player = None

        if target_player is not None:
            zone = self.game.zones[zone_name, target_player.id]
        else:
            zone = self.game.zones[zone_name]

        player.write(zone)
        player.write("-" * len(str(zone)))
        for obj in zone.objects:
            player.write(obj)

    def handle_info(self, player, args):
        if len(args) < 1:
            player.write("info <zone>")
            return

        if args[0] == "library" or args[0] == "l":
            self.print_zone(player, "library", args[1:])

        elif args[0] == "hand" or args[0] == "h":
            self.print_zone(player, "hand", args[1:])

        elif args[0] == "graveyard" or args[0] == "g":
            self.print_zone(player, "graveyard", args[1:])

        elif args[0] == "exile" or args[0] == 'e':
            self.print_zone(player, "exile")

        elif args[0] == "battlefield" or args[0] == "b":
            self.print_zone(player, "battlefield")

        elif args[0] == "stack" or args[0] == "s":
            self.print_zone(player, "stack")

        else:
            player.write("Invalid target for 'info' command: '{}'".format(args[0]))

    def handle_cast(self, player, args):
        if len(args) < 1:
            player.write("cast <object_id>")
            return

        target = self.find_object(args[0])

        if target is None:
            player.write("Object '{}' not found".format(args[0]))
            return

        player.write(target)

        #self.game.queue


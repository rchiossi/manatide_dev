import uuid

from manatide.core.deck import Deck

class Player(object):
    def __init__(self, game):
        if game is None:
            log.e("No game provided for player")

        self.id = uuid.uuid4()
        self.deck = None

        self.game = game

    def read(self):
        log.e("Player read() unimplemented")

    def write(selfi, cmd):
        log.e("Player write() unimplemented")

    def load_deck(self):
        log.e("Player load_deck() unimplemented")

    def __str__(self):
        return "Player[{}]".format(self.id.hex[:8])


from manatide.core.event import EventQueueStatus
import readline
class ConsolePlayer(Player):
    def read(self):
        if self.game.event_queue.status == EventQueueStatus.BUSY:
            return None

        elif self.game.event_queue.status == EventQueueStatus.IDLE:
            if self.id != self.game.players[0].id:
                return None

            print()
            cmd = input('{}: '.format(self))
            print()

            return cmd

        return None

    def write(self, cmd):
        print('>: {}'.format(cmd))

    def load_deck(self):
        #TODO: remove hardcoded deck name
        self.deck = Deck("test_deck.txt")




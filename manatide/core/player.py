import uuid

from manatide.core.deck import Deck

class Player(object):
    def __init__(self, deckname):
        if deckname is None:
            log.e("Invalid deck name")

        self.id = uuid.uuid4()

        self.deck = Deck(deckname)

    def read():
        log.e("Player read() unimplemented")

    def write():
        log.e("Player write() unimplemented")

    def __str__(self):
        return "Player[{}]".format(self.id.hex[:8])


class ConsolePlayer(Player):
    def read(self):
        return input('{}: '.format(self))

    def write(self, cmd):
        print('>: {}'.format(cmd))




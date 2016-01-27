import uuid

from manatide.deck import Deck

class Player(object):
    def __init__(self, deckname, read_cb, write_cb):
        if deckname is None:
            log.e("Invalid deck name")

        self.id = uuid.uuid4()

        self.deck = Deck(deckname)

        self.read = read_cb
        self.write = write_cb


import re
import uuid

from util.log import log

class Deck(object):
    def __init__(self, filename=None):
        self.id = uuid.uuid4()
        self.filename = filename
        self.main = {}
        self.side = {}

        if filename is None:
            return

        with open(filename) as f:
            data = f.read()

        in_sideboard = False
        for line in data.split('\n'):
            if not line.strip():
                in_sideboard = True
                continue

            exp = re.search("([0-9]+) (.+)", line.strip())
            amount = exp.group(1)
            card = exp.group(2)

            if not in_sideboard:
                self.main[card] = amount
            else:
                self.side[card] = amount

    def __str__(self):
        return "Deck[{}]".format(self.id)


import importlib
import re
import uuid

from util.log import log

class Deck(object):
    def __init__(self, filename=None):
        self.id = uuid.uuid4()
        self.filename = filename
        self.main = []
        self.side = []

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
            amount = int(exp.group(1))
            cardname = exp.group(2)

            filename = Deck.get_file_name(cardname)
            classname = Deck.get_class_name(cardname)

            log.w("cards.{}.{}".format(filename, classname))

            try:
                card = importlib.import_module("cards.{}".format(filename))
                card = getattr(card, classname)
            except:
                log.e("Card not found: {}".format(cardname))

            for i in range(amount):
                if not in_sideboard:
                    self.main.append(card())
                else:
                    self.side.append(card())

    @staticmethod
    def get_file_name(cardname):
        name = cardname.lower()
        name = name.replace(" ", "_")
        name = name.replace("'", "")
        name = name.replace('æ','ae')

        return name

    def get_class_name(cardname):
        name = cardname.lower()
        name = name.replace("'", "")
        name = name.replace('æ','ae')
        name = name.title()
        name = name.replace(" ", "")

        return name

    def __str__(self):
        return "Deck[{}]".format(self.id)


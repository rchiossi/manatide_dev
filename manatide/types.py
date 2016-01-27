from enum import Enum

class Types(Enum):
    ARTEFACT = 0
    CONSPIRACY = 1
    CREATURE = 2
    ENCHANTMENT = 3
    INSTANT = 4
    LAND = 5
    PHENOMENON = 6
    PLANE = 7
    PLANESWALKER = 8
    SCHEME = 9
    TRIBAL = 10
    VANGUARD = 11

class SuperTypes(Enum):
    BASIC = 0
    LEGENDARY = 1
    ONGOING = 2
    SNOW = 3
    WORLD = 4

class ArtefactTypes(Enum):
    CONTRAPTION = 0
    EQUIPMENT = 1
    FORTIFICATION = 2

class EnchantmentTypes(Enum):
    AURA = 0
    CURSE = 1
    SHRINE = 2

class LandTypes(Enum):
    DESERT = 0
    FOREST = 1
    GATE = 2
    ISLAND = 3
    LAIR = 4
    LOCUS = 5
    MINE = 6
    MOUNTAIN = 7
    PLAINS = 8
    POWERPLANT = 9
    SWAMP = 10
    TOWER = 11
    URZAS = 12

class PlaneswalkerTypes(Enum):
    AJANI = 0
    ASHIOK = 1
    BOLAS = 2
    CHANDRA = 3
    DACK = 4
    DARETTI = 5
    DOMRI = 6
    ELSPETH = 7
    FREYALISE = 8
    GARRUK = 9
    GIDEON = 10
    JACE = 11
    KARN = 12
    KIORA = 13
    KOTH = 14
    LILIANA = 15
    NAHIRI = 16
    NARSET = 17
    NISSA = 18
    NIXILIS = 19
    RAL = 20
    SARKHAN = 21
    SORIN = 22
    TAMIYO = 23
    TEFERI = 24
    TEZZERET = 25
    TIBALT = 26
    UGIN = 27
    VENSER = 28
    VRASKA = 29
    XENAGOS = 30

class SpellTypes(Enum):
    ARCANE = 0
    TRAP = 1

class CreatureTypes(Enum):
    ADVISOR = 0
    ALLY = 1
    ANGEL = 2
    ANTELOPE = 3
    APE = 4
    ARCHER = 5
    ARCHON = 6
    ARTIFICER = 7
    ASSASSIN = 8
    ASSEMBLY-WORKER = 9
    ATOG = 10
    AUROCHS = 11
    AVATAR = 12
    BADGER = 13
    BARBARIAN = 14
    BASILISK = 15
    BAT = 16
    BEAR = 17
    BEAST = 18
    BEEBLE = 19
    BERSERKER = 20
    BIRD = 21
    BLINKMOTH = 22
    BOAR = 23
    BRINGER = 24
    BRUSHWAGG = 25
    CAMARID = 26
    CAMEL = 27
    CARIBOU = 28
    CARRIER = 29
    CAT = 30
    CENTAUR = 31
    CEPHALID = 32
    CHIMERA = 33
    CITIZEN = 34
    CLERIC = 35
    COCKATRICE = 36
    CONSTRUCT = 37
    COWARD = 38
    CRAB = 39
    CROCODILE = 40
    CYCLOPS = 41
    DAUTHI = 42
    DEMON = 43
    DESERTER = 44
    DEVIL = 45
    DJINN = 46
    DRAGON = 47
    DRAKE = 48
    DREADNOUGHT = 49
    DRONE = 50
    DRUID = 51
    DRYAD = 52
    DWARF = 53
    EFREET = 54
    ELDER = 55
    ELDRAZI = 56
    ELEMENTAL = 57
    ELEPHANT = 58
    ELF = 59
    ELK = 60
    EYE = 61
    FAERIE = 62
    FERRET = 63
    FISH = 64
    FLAGBEARER = 65
    FOX = 66
    FROG = 67
    FUNGUS = 68
    GARGOYLE = 69
    GERM = 70
    GIANT = 71
    GNOME = 72
    GOAT = 73
    GOBLIN = 74
    GOD = 75
    GOLEM = 76
    GORGON = 77
    GRAVEBORN = 78
    GREMLIN = 79
    GRIFFIN = 80
    HAG = 81
    HARPY = 82
    HELLION = 83
    HIPPO = 84
    HIPPOGRIFF = 85
    HOMARID = 86
    HOMUNCULUS = 87
    HORROR = 88
    HORSE = 89
    HOUND = 90
    HUMAN = 91
    HYDRA = 92
    HYENA = 93
    ILLUSION = 94
    IMP = 95
    INCARNATION = 96
    INSECT = 97
    JELLYFISH = 98
    JUGGERNAUT = 99
    KAVU = 100
    KIRIN = 101
    KITHKIN = 102
    KNIGHT = 103
    KOBOLD = 104
    KOR = 105
    KRAKEN = 106
    LAMIA = 107
    LAMMASU = 108
    LEECH = 109
    LEVIATHAN = 110
    LHURGOYF = 111
    LICID = 112
    LIZARD = 113
    MANTICORE = 114
    MASTICORE = 115
    MERCENARY = 116
    MERFOLK = 117
    METATHRAN = 118
    MINION = 119
    MINOTAUR = 120
    MONGER = 121
    MONGOOSE = 122
    MONK = 123
    MOONFOLK = 124
    MUTANT = 125
    MYR = 126
    MYSTIC = 127
    NAGA = 128
    NAUTILUS = 129
    NEPHILIM = 130
    NIGHTMARE = 131
    NIGHTSTALKER = 132
    NINJA = 133
    NOGGLE = 134
    NOMAD = 135
    NYMPH = 136
    OCTOPUS = 137
    OGRE = 138
    OOZE = 139
    ORB = 140
    ORC = 141
    ORGG = 142
    OUPHE = 143
    OX = 144
    OYSTER = 145
    PEGASUS = 146
    PENTAVITE = 147
    PEST = 148
    PHELDDAGRIF = 149
    PHOENIX = 150
    PINCHER = 151
    PIRATE = 152
    PLANT = 153
    PRAETOR = 154
    PRISM = 155
    PROCESSOR = 156
    RABBIT = 157
    RAT = 158
    REBEL = 159
    REFLECTION = 160
    RHINO = 161
    RIGGER = 162
    ROGUE = 163
    SABLE = 164
    SALAMANDER = 165
    SAMURAI = 166
    SAND = 167
    SAPROLING = 168
    SATYR = 169
    SCARECROW = 170
    SCION = 171
    SCORPION = 172
    SCOUT = 173
    SERF = 174
    SERPENT = 175
    SHADE = 176
    SHAMAN = 177
    SHAPESHIFTER = 178
    SHEEP = 179
    SIREN = 180
    SKELETON = 181
    SLITH = 182
    SLIVER = 183
    SLUG = 184
    SNAKE = 185
    SOLDIER = 186
    SOLTARI = 187
    SPAWN = 188
    SPECTER = 189
    SPELLSHAPER = 190
    SPHINX = 191
    SPIDER = 192
    SPIKE = 193
    SPIRIT = 194
    SPLINTER = 195
    SPONGE = 196
    SQUID = 197
    SQUIRREL = 198
    STARFISH = 199
    SURRAKAR = 200
    SURVIVOR = 201
    TETRAVITE = 202
    THALAKOS = 203
    THOPTER = 204
    THRULL = 205
    TREEFOLK = 206
    TRISKELAVITE = 207
    TROLL = 208
    TURTLE = 209
    UNICORN = 210
    VAMPIRE = 211
    VEDALKEN = 212
    VIASHINO = 213
    VOLVER = 214
    WALL = 215
    WARRIOR = 216
    WEIRD = 217
    WEREWOLF = 218
    WHALE = 219
    WIZARD = 220
    WOLF = 221
    WOLVERINE = 222
    WOMBAT = 223
    WORM = 224
    WRAITH = 225
    WURM = 226
    YETI = 227
    ZOMBIE = 228
    ZUBERA = 229

class PlaneTypes(Enum):
    ALARA = 0
    ARKHOS = 1
    AZGOL = 2
    BELENON = 3
    BOLAS’S MEDITATION REALM = 4
    DOMINARIA = 5
    EQUILOR = 6
    ERGAMON = 7
    FABACIN = 8
    INNISTRAD = 9
    IQUATANA = 10
    IR = 11
    KALDHEIM = 12
    KAMIGAWA = 13
    KARSUS = 14
    KEPHALAI = 15
    KINSHALA = 16
    KOLBAHAN = 17
    KYNETH = 18
    LORWYN = 19
    LUVION = 20
    MERCADIA = 21
    MIRRODIN = 22
    MOAG = 23
    MONGSENG = 24
    MURAGANDA = 25
    NEW = 26
    PHYREXIA = 27
    PHYREXIA = 28
    PYRULEA = 29
    RABIAH = 30
    RATH = 31
    RAVNICA = 32
    REGATHA = 33
    SEGOVIA = 34
    SERRA’S REALM = 35
    SHADOWMOOR = 36
    SHANDALAR = 37
    ULGROTHA = 38
    VALLA = 39
    VRYN = 40
    WILDFIRE = 41
    XEREX = 42
    ZENDIKAR. = 43


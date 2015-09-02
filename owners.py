ALCHEMIST='Alchemist'
BARDIC_COLLEGE='Bardic College'
CABAL='Cabal'
CASTERS_TOWER="Caster's Tower"
CASTLE='Castle'
CULT='Cult'
DANCE_HALL='Dance Hall'
GENERIC='Generic'
GUILDHALL='Guildhall'
HERBALIST='Herbalist'
HOUSE='House'
INN='Inn'
LIBRARY='Library'
MAGICAL_ACADEMY='Magical Academy'
MAGIC_SHOP='Magic Shop'
MENAGERIE='Menagerie'
MERCENARY_COMPANY='Mercenary Company'
MILITARY_ACADEMY='Military Academy'
MONASTERY='Monastery'
SHOP='Shop'
SMITHY='Smithy'
STABLE='Stable'
TAVERN='Tavern'
TEMPLE='Temple'
THEATER='Theater'
THIEVES_GUILD="Thieves' Guild"


class PlayerHoldings:
    def __init__(self,name,holdings):
        self.name=name
        self.holdings=holdings

    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name



from event_data_service import  EventObjects
from owners import PlayerHoldings
import owners as o

import random
from random import choice
import sys


class EventTumbler:
    def __init__(self):
        self.starting_chance=.2
        self.current_chance=self.starting_chance
    def __iter__(self):
        return self
    def next(self):
        if self.current_chance<=random.random():
            self.current_chance = self.starting_chance
            return True
        else:
            self.current_chance+=.05
            return False

class EventEngine:
    def __init__(self,players,events):
        self.p = players;
        self.e = events;
        self.tumbler = EventTumbler()

    def __iter__(self):
        return self
    def next(self):
        if self.tumbler.next():
            #add event picking logic
            player = choice(self.p)
            eventTable = choice(player.holdings)
            #ok now roll in the generic table
            generic_event = EventObjects[o.GENERIC].getEvent()
            if generic_event.startswith("Building-Specific Event:"):
                event = EventObjects[eventTable].getEvent()
            else:
                event = generic_event
            return player, eventTable, event

        else:
            return None;


#CONFIG
DATA_FILE='data/events.csv'



#/CONFIG
import csv
from random import choice
import sys
d100=lambda:choice(range(1,101))


class EventTable:
    def __init__(self):
        self.eventRows = {}
        pass

    def __str__(self):
        return repr(self.eventRows)

    def __repr__(self):
        return repr(self.eventRows)

    def addRow(self,row):
        self.eventRows[(row[1],row[2])]=row[3:]

    def getEvent(self):
        roll=d100()
        for low,high in self.eventRows:
            if roll>=int(low) and roll<=int(high):
                return self.eventRows[(low,high)][-1] 
        return roll


EventObjects = {}
with open(DATA_FILE) as csvfile:
    reader = csv.reader(csvfile)
    reader.next()
    for row in reader:
        if not EventObjects.has_key(row[0]):
            EventObjects[row[0]]=EventTable()
        EventObjects[row[0]].addRow(row)
        
        
if __name__ == '__main__':
    print EventObjects['Guildhall']
    print EventObjects

import csv
from random import choice
d100=lambda:choice(range(1,101))


class EventTable:
	def __init__(self):
		self.eventRows = []
		pass
	def addRow(self,row):
		self.eventRows.append(row)
	def getRandomRow(self):
		roll=d100()
names = {}
rows = []
with open('data/events.csv') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		rows.append(row)
		if not names.has_key(row[0]):
			names[row[0]]=EventTable()
		names[row[0]].addRow(row)
		
		
print names['Guildhall']
print names.keys()

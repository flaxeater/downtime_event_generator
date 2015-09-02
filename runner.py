from EventEngine import EventEngine
from event_data_service import EventObjects
import owners as o
from owners import PlayerHoldings as p


from sys import exit;

def get_all_events_tables_for_printing():
    ret = []
    #print sorted(EventObjects.keys());exit();
    for event in sorted(EventObjects.keys()):
        table=[]
        eventRows=EventObjects[event].eventRows
        for key in sorted(eventRows.keys(), lambda x,y:int(x[0]) - int(y[0])):
            table.append({'range':key,'body':eventRows[key]})
        ret.append({'name':event,'table':table})
    return ret


encoded_player_data=[
    p('Cain',[o.MILITARY_ACADEMY,o.MERCENARY_COMPANY]),
    p('Oz',[o.MAGICAL_ACADEMY,o.ALCHEMIST,o.LIBRARY]),
    p('sirus',[o.TEMPLE,o.SHOP,o.HOUSE]),
    p('shazaman',[o.THIEVES_GUILD,o.CABAL,o.CULT])
]
engine = EventEngine(encoded_player_data,EventObjects);


events=[]
for x in range(365):
    events.append(engine.next());


for x in events:
    print x

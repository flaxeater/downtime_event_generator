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
            table.append({'range':key,'body':eventRows[key][-1]})
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

output="""
<html>
<head>
<title>High Level Campaign Rannick Event List</title>
</head>
<body>
<table border="1">
"""
for table in get_all_events_tables_for_printing():
    output+='<tr style="background-color: lightgray;"><td colspan="2">%s</td></tr>' %table['name']
    output+="\n";
    for row in table['table']:
        output+='<tr><td width="200px" align="center">%s</td><td>%s</td></tr>' %(str(row['range']),row['body'])
        output+="\n";
output+="</table>"
output+="""
<table border="2">
<thead>
<td colspan="4"><h1>EVENTS</h1></td>
</thead>
<tr><td>Day</td><td>Name</td><td>Origin</td><td>Description</td></tr>
"""
days = 1;
for event in events:
    if event:
        output+="""
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
        </tr>
        """ %(str(days),str(event[0]),str(event[1]),str(event[2]))
    else:
        output+="""
        <tr><td>%s</td><td colspan="3"></td></tr>
        """ %days
    days+=1

output+="</body></html>"
print output

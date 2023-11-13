import json

filename = "new_data/new_event_role_multiplicities.txt"
events = {}
idx = 1
for line in open(filename).readlines():
    if (line.strip() != ""):
        jsonitem = {}
    
        event_id = str(idx)
        while len(event_id) < 3:
            event_id = "0"+event_id
        event_id = "evt"+event_id
        jsonitem["event_id"] = event_id
    
        items = line.split()
    
        roles = []
        itemidx = 1
        while itemidx < len(items):
            for i in range(int(items[itemidx+1])):
                roles.append(items[itemidx])
            itemidx += 2
        jsonitem["roles"] = roles
    
        jsonitem["i-label"] = idx
    
        jsonitem["keywords"] = []
    
        events[items[0]] = jsonitem
    
    idx += 1
outfile=open("format.json",mode='w')
json.dump(events, outfile, indent=2)
outfile.close()
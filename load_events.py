from event_format import event_format
import json
class eventContainer:
    def __init__(self, jsonlinesFIlename, eventFormats = None):
        if (eventFormats == None):
            eventFormats = event_format()
        self.eventsByType = []
        self.eventsAll = []
        f = open(jsonlinesFIlename)
        for jsonline in f:
            event = json.loads(jsonline)
            toAppend = {}
            if (event["gold_evt_links"] == []):
                continue
            event_id = int(event["gold_evt_links"][0][2][3:6])
            while len(self.eventsByType) < event_id:
                self.eventsByType.append([])
            toAppend["i-label"] = event_id
            
            eventFormat = eventFormats.getEventFormatByIndex(event_id)
            
            toAppend["text"] = []
            for sentence in event["sentences"]:
                for word in sentence:
                    toAppend["text"].append(word)
            
            keyword = ""
            for i in range(event["gold_evt_links"][0][0][0], event["gold_evt_links"][0][0][0]+1):
                keyword += toAppend["text"][i]+" "
            keyword = keyword[:-1]
            if keyword not in eventFormat["keywords"]:
                eventFormats.addKeyWords(event_id, keyword)
            
            toAppend["roles"] = []
            roles = eventFormat["roles"]
            for gold_event in event["gold_evt_links"]:
                temp = ""
                for j in range(gold_event[1][0],gold_event[1][1]+1):
                    temp += toAppend["text"][j]+" "
                role = roles[int(gold_event[2][9:11])-1]
                toAppend["roles"].append((role, temp[:-1], gold_event[1][0]))
            self.eventsByType[event_id-1].append(len(self.eventsAll))
            self.eventsAll.append(toAppend)
    def getEventsById(self, index, argumentTypes = None):
        toReturn = []
        for i in self.eventsByType[index-1]:
            if argumentTypes == None:
                toReturn.append(self.eventsAll[i])
            else:
                match = (len(argumentTypes) == len(self.eventsAll[i]["roles"]))
                if match:
                    for j in range(len(argumentTypes)):
                        match = match and argumentTypes[j] == self.eventsAll[i]["roles"][j][0]
                if match:
                    toReturn.append(self.eventsAll[i])
        return toReturn
        return [self.eventsAll[i] for i in self.eventsByType[index-1]]    

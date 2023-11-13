import json
FILENAME = "format.json"
class event_format:
    def __init__(self, filename = FILENAME):
        self.filename = filename
        f = open(filename)
        self.eventdict = json.load(f)
        f.close()
        
    def getEventFormatByIndex(self, index):
        for v in self.eventdict.values():
            if (v["i-label"]) == index:
                return v
        return None
    
    def getEventNameByIndex(self, index):
        for k in self.eventdict.keys():
            if (self.eventdict[k]["i-label"]) == index:
                return k
        return None
    
    def getEventFormatByName(self, name):
        return self.eventdict.get(name)
    
    def addKeyWords(self, index, keyword):
        for v in self.eventdict.values():
            if (v["i-label"]) == index:
                v["keywords"].append(keyword)
    
    def updateFile(self):
        outfile = open(self.filename,mode='w')
        json.dump(self.eventdict, outfile, indent=2)
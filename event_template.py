import json
FILENAME = "template.json"
class event_template:
    def __init__(self, filename = FILENAME):
        self.filename = filename
        f = open(filename)
        self.eventdict = json.load(f)
        f.close()
        
    def getEventTemplateByIndex(self, index):
        for v in self.eventdict.values():
            if index in (v["i-labels"]):
                return v
        return None
    
    # def addKeyWords(self, index, keyword):
    #     for v in self.eventdict.values():
    #         if index in (v["i-labels"]):
    #             v["keywords"].append(keyword)
    
    def updateFile(self):
        outfile = open(self.filename,mode='w')
        json.dump(self.eventdict, outfile, indent=2)
        
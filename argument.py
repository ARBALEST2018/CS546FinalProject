import event
class argument:
    name = ""
    attributes = {}
    participate = {}
    
    def __init__(self, name):
        self.name = name
        
    def addAttribute(self, attributeName, attributeContent):
        if self.attributes.get(attributeName) == None:
            self.attributes[attributeName] = []
        self.attributes[attributeName].append(attributeContent)
        
    def addParticipate(self, participateName, participateContent):
        if self.participate.get(participateName) == None:
            self.participate[participateName] = []
        self.participate[participateName].append(participateContent)
        
    def getName(self):
        return self.name
    
    def getAttribute(self, attributeName):
            return self.attributes.get(attributeName)
    
    def getAttributeNames(self):
        return self.attributes.keys()
    
    def getParticipate(self, participateName):
            return self.participate.get(participateName)
    
    def getParticipateNames(self):
        return self.participate.keys()
    
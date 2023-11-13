import argument
class Event:
    name = ""
    properties = {}
    
    def __init__(self, name):
        self.name = name
        
    def addProperty(self, propertyName, propertyContent):
        if self.properties.get(propertyName) == None:
            self.properties[propertyName] = []
        self.properties[propertyName].append(propertyContent)
        
    def getName(self):
        return self.name
    
    def getProperty(self, propertyName):
        return self.properties.get(propertyName)
    
    def getPropertyNames(self):
        return self.properties.keys()
    
    
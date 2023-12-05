import json
FILENAME = "new_data/test.json"
class predictionContainer:
    def __init__(self, filename = FILENAME):
        self.filename = filename
        f = open(self.filename)
        self.predictionsDict = json.load(f)
        f.close()
    def getPredictionByDocKey(self, doc_key):
        if (self.predictionsDict.get(doc_key) == None):
            return []
        return self.predictionsDict.get(doc_key)
    def updatePrediction(self, doc_key, prediction):
        self.predictionsDict[doc_key] = prediction
    def updateFile(self):
        outfile = open(self.filename,mode='w')
        json.dump(self.predictionsDict, outfile, indent=4)
        outfile.close()
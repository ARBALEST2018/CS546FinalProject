import json
from load_events import eventContainer
from predictions import predictionContainer

testEventContainer = eventContainer("rams//data/test.jsonlines")
samplePredictions = predictionContainer("new_data/test-sample-gpt4.json")
templatePredictions = predictionContainer("new_data/test-template.json")
outputfile = open("SampleOutputComparison.txt", mode='w', encoding='utf-8')
outputfileByType = open("SampleOutputComparisonByTypeWith#.txt", mode='w', encoding='utf-8')
outputfileBoth = open("BothOutputComparisonByTypeWith#.txt", mode='w', encoding='utf-8')
types = []
typet = []
for key in samplePredictions.predictionsDict.keys():
    testEvent = testEventContainer.getEventByDocKey(key)
    
    samplePrediction = samplePredictions.getPredictionByDocKey(key)
    samplePredictionArgs = json.loads(samplePrediction[len(samplePrediction)-1]["content"])
    skip = False
    for v in samplePredictionArgs.values():
        if isinstance(v, list) or isinstance(v, dict):
            skip = True
            break
    if (skip):
        continue
    
    while len(types) < testEvent["i-label"]:
        types.append([])
    
    text = ""
    for word in testEvent["text"]:
        if (word != "."):
            text += word+" "
        else:
            text += word+"\n"
    toAppend = text+"\n"
    outputfile.write(text+"\n")
    toAppend += "Type "+str(testEvent["i-label"])+" (#"+str(len(types[testEvent["i-label"]-1])+1)+") : "+testEvent["event_type"]+"\n"
    outputfile.write("Type "+str(testEvent["i-label"])+" : "+testEvent["event_type"]+"\n")
    
    line = "Gold: "
    for v in testEvent["roles"]:
        line += v[1]+", "
    toAppend += line[:-2]+"\n"
    outputfile.write(line[:-2]+"\n")
    
    line = "Pred: "
    for v in samplePredictionArgs.values():
        line += v+", "
    toAppend += line[:-2]+"\n"
    outputfile.write(line[:-2]+"\n")

    outputfile.write("\n\n\n")
    types[testEvent["i-label"]-1].append(toAppend+"\n\n\n")
    
    templatePrediction = templatePredictions.getPredictionByDocKey(key)
    if len(templatePrediction) == 0:
        continue
    templatesamplePredictionArgs = json.loads(templatePrediction[len(templatePrediction)-1]["content"])
    for v in templatesamplePredictionArgs.values():
        if isinstance(v, list) or isinstance(v, dict):
            skip = True
            break
    if (skip):
        continue   
    
    while len(typet) < testEvent["i-label"]:
        typet.append([])
    line = "Temp: "
    for v in templatesamplePredictionArgs.values():
        line += v+", "
    toAppend += line[:-2]+"\n"
    typet[testEvent["i-label"]-1].append(toAppend+"\n\n\n")
    
    
    
for type in types:
    for item in type:
        outputfileByType.write(item)

for type in typet:
    for item in type:
        outputfileBoth.write(item)

outputfileBoth.close()
outputfileByType.close()
outputfile.close()
    

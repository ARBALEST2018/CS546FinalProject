import csv
import configs
import openai
import os
import event
import argument
import nltk
import json
import string
from collections.abc import Iterable
from event_format import event_format
from load_events import eventContainer

openai.api_key = configs.OPENAI_CHAT_API_KEY


# def extract_event(sentence):
#     temp = {"user": sentence+" "+configs.EVENT_EXT}
#     print(ask_openai(temp))
    
# def extract_arguments(sentence):
#     temp = {"user": sentence+" "+configs.ARGUMENT_EXT}
#     temp = ask_openai(temp)
#     # print(temp)
#     toReturn = []
#     for line in temp["content"].split("\n"):
#         words = tokenizer.tokenize(line)
#         toAppend = ""
#         for word in words:
#             if not word.isnumeric():
#                 toAppend+=word+" "
#         toReturn.append(toAppend.strip())
#     return toReturn
        

# def loadjsonlines(inputfilename,outputwriter = None, process = None):
#     f = open(inputfilename)
#     for jsonline in open(inputfilename):
#         temp = json.loads(jsonline)
#         if (process != None):
#             temp = process(temp)
#         if (outputwriter != None):
#             outputwriter(temp)
        
# def process(input):
#     toReturn = []
#     words = []
#     sentences = []
#     for sentence in input["sentences"]:
#         temp = ""
#         first = True
#         for word in sentence:
#             words.append(word)
#             if word in string.punctuation or first:
#                 temp += word
#             else:
#                 temp += (" "+word)
#             first = False
        
#         sentences.append(temp)
#     triplets = []
#     for triplet in input["gold_evt_links"]:
#         tri = ""
#         for i in range(0,2):
#             temp = ""
#             for j in range(triplet[i][0], triplet[i][1]+1):
#                 temp += words[j]
#                 temp += " "
#             tri += temp + " : "
#         tri += triplet[2]
#         triplets.append(tri)
#     return [sentences,triplets]
    
# n = "test"

# w = open("new_data/"+n+".txt", mode='w', encoding='utf-8')    

# def outwriter(input):
#     if isinstance(input, list):
#         for item in input:
#             outwriter(item)
#         w.write("\n")
#     else:
#         w.write(input+"\n")

# loadjsonlines("rams/data/"+n+".jsonlines", process=process, outputwriter=outwriter)






# n = "dev"

# jsonlinesToOpen = "rams/data/"+n+".jsonlines"
# w = open("new_data/"+n+".txt", mode='w', encoding='utf-8')
# with open(jsonlinesToOpen) as f:
#     i = 0
#     for line in f:
#         jsonline = json.loads(line)
#         if i < 2:
#             for sentence in jsonline["sentences"]:
#                 temp = ""
#                 first = True
#                 for word in sentence:
#                     temp += word+" "
#                 w.write(temp[:-1]+"\n")
#             w.write("\n")


def makePrompt(trainEventContainer, testEvent, max_num, with_location = True):
    toReturn = ""
    if with_location:
        toReturn += configs.PROMPT_0+"\n"+"\n"
    else:
        toReturn += configs.PROMPT_0_NL+"\n"+"\n"
    trainEvents = trainEventContainer.getEventsById(testEvent["i-label"], [role[0] for role in testEvent["roles"]])
    if (len(trainEvents)) == 0:
        return ""
    i = 0
    while i < len(trainEvents) and i < max_num:
        trainEvent = trainEvents[i]
        
        text = ""
        for word in trainEvent["text"]:
            text += word+" "
        text = configs.PROMPT_TEXT+str(i+1)+" : "+text[:-1]+"\n"
        
        # ats = ""
        # acs = ""
        # als = ""
        
        for role in trainEvent["roles"]:
            toAdd = role[0]+" : "+role[1]
            if with_location:
                # als += str(role[2])+" , "
                toAdd += " ("+str(role[2])+")"
            text += toAdd+"\n"
            # ats += str(role[0])+" , "
            # acs += str(role[1])+" , "
            
        # text += configs.PROMPT_EVENT_ARGUMENT_TYPE+str(i+1)+" : "+ats[:-3]+"\n"
        # text += configs.PROMPT_EVENT_ARGUMENT_CONTENT+str(i+1)+" : "+acs[:-3]+"\n"
        # if with_location:
        #     text += configs.PROMPT_EVENT_ARGUMENT_LOCATION+str(i+1)+" : "+als[:-3]+"\n"
        text += "##\n"
        toReturn += text
        i += 1
    if with_location:
        toReturn += "\n"+configs.PROMPT_1+"\n"+"\n"
    else:
        toReturn += "\n"+configs.PROMPT_1_NL+"\n"+"\n"
    text = ""
    for word in testEvent["text"]:
        text += word+" "
    toReturn += configs.PROMPT_TEXT+str(i+1)+" : "+text[:-1]+"\n"
    # ats = ""
    for role in testEvent["roles"]:
        toReturn += role[0]+" : \n"
    #     ats += str(role[0])+" , "
    # toReturn += configs.PROMPT_EVENT_ARGUMENT_TYPE+str(i+1)+" : "+ats[:-3]+"\n"
    # toReturn += configs.PROMPT_EVENT_ARGUMENT_CONTENT+str(i+1)+" : "+"\n"
    if with_location:
        toReturn += configs.PROMPT_EVENT_ARGUMENT_LOCATION+str(i+1)+" : "+"\n"
    return toReturn
        
class writer:
    def write(a):
        print(a,end="")
        
eventFormats = event_format()
trainEventContainer = eventContainer("rams//data/train.jsonlines",eventFormats=eventFormats)
# json.dump(trainEventContainer.eventsAll, open("train_events.json", mode='w'), indent=4)
eventFormats.updateFile()
testEventContainer = eventContainer("rams//data/test.jsonlines")
# json.dump(testEventContainer.eventsAll, open("test_events.json", mode='w'), indent=4)
predictionToWrite = open("new_data/test-pred.txt",mode='w',encoding='utf-8')
outputToWrite = open("new_data/output.txt",mode='w',encoding='utf-8')
counter = 0
for testEvent in testEventContainer.eventsAll:
    prompt = makePrompt(trainEventContainer, testEvent, 8, False)
    if (len(prompt) == 0):
        continue
    print()
    outputToWrite.write("\n")
    print(prompt)
    outputToWrite.write(prompt)
    print()
    outputToWrite.write("\n")
    text = ""
    for word in testEvent["text"]:
        if (word != "."):
            text += word+" "
        else:
            text += word+"\n"
    predictionToWrite.write(text+"\n")
    response = openai.Completion.create(
        model=configs.OPENAI_TEXT_MODEL,
        prompt=prompt,
    )
    predictionToWrite.write(response["choices"][0]["text"]+"\n\n")
    print(response)
    outputToWrite.write(response["choices"][0]["text"])
    print()
    outputToWrite.write("\n\n\n")
    counter += 1
    
    # if (counter >= 10):
    #     break
predictionToWrite.close()


















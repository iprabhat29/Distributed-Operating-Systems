
# Contributors:
#    Prabhat Bhatt 
#	Apoorva SAxena

"""
This is REST API implemention by using flask restful. This module handle all the REST API implementation for Obelix and clients
Contains two type of methods [GET] and [PUT].
"""
from flask import Flask
import json
from flask import jsonify
from flask import request
app = Flask(__name__)
import threading
from thread import *
import requests
#################Get everything#######################################
@app.route('/getMedalTally/',methods= ['GET'])
def getMedalTallyall():
  with open('dos_data.json','r') as files:
    data = json.load(files)
  dat1 = data['Team']['Gual']
  dat2 = data['Team']['Rome']
  dat1.pop('Stone Skating',0)
  dat1.pop('Stone Curling',0)
  dat1.pop('Stone Throwing',0)
  dat2.pop('Stone Skating',0)
  dat2.pop('Stone Curling',0)
  dat2.pop('Stone Throwing',0)
  return jsonify({'Gual':dat1},{'Rome':dat2})


#################Get Medal Tally of a Team#######################################
"""
	This is a GET method which reads the database file and returns medal tally for <teamName>
"""
@app.route('/getMedalTally/<teamName>',methods = ['GET'])
def getteam(teamName):
  with open('dos_data.json','r') as files:
    data = json.load(files)
  for e in data['Team']:
    if e == teamName:
      dat = data['Team'][e]
  dat.pop('Stone Curling',0)
  dat.pop('Stone Throwing',0)
  dat.pop('Stone Skating',0)
  return jsonify({teamName:dat})



#################Get Score of a Team#############################################

"""
	This is a GET method which reads the data return the score for a specific <eventType>.
	For example <eventType> = 'Stone Curling' will give score of Rome and Gaul for the event Stone Curling 
"""

@app.route('/getScore/<eventType>/',methods= ['GET'])
def getscore(eventType):
 with open('dos_data.json','r') as files:
  data = json.load(files)
  dat1 = data['Team']['Gual'][eventType]['Score']
  dat2 = data['Team']['Rome'][eventType]['Score']
 return jsonify({'Gual':dat1},{'Rome':dat2})

#################Increement Medal Tally#########################################

"""
	This is a PUT method which increment specific <medalType> for specific <teamName>.
	It does an internal authentication check if the sender of this request is Cacofonix.
	For example if medalType is Gold and <teamName> is Rome it will incumbent the Gold
 	tally of Rome by 1
"""

@app.route('/incrementMedalTally/<teamName>/<medalType>/<auth_id>/',methods=['PUT'])
def updateEmpattr(teamName,medalType,auth_id):
  if auth_id == 'Cacofonix':
    with open('dos_data.json','r') as files:
      data = json.load(files)
    for e in data['Team']:
        if e == teamName:
          if medalType == 'Gold':
            data['Team'][teamName]['Gold'] +=1 
          if medalType == 'Silver':
            data['Team'][teamName]['Silver'] += 1
          if medalType == 'Bronze':
            data['Team'][teamName]['Bronze'] += 1

    with open('dos_data.json','w') as fp:
      json.dump(data,fp,indent = 4)
    return jsonify({teamName:data['Team'][teamName]})



#################Set Score for an event#########################################
"""
	This is a PUT method which updates the score of Rome and Gaul teams for specified <eventType>.
	It does and internal authentication check if the sender of this request is Cacofonix.
	After updating the score a push notification goes to the clients who are subscribed to this event.
	For example if <eventType> is Stone Curling it will update the score with the score provided
	<gaul_score>,<rome_score>.After update all the clients who are subscribed to <Stone Curling> will 
	be updated with the new score.
	The important part in this is that a client is added to our database only if it is subscribed to 
	Stone Curling since we are considering only Stone Curling example.This can be expanded further for 
	other events.
"""
@app.route('/setScore/<eventType>/<rome_score>/<gaul_score>/<auth_id>',methods=['PUT'])
def setscore(eventType,rome_score,gaul_score,auth_id):
  if auth_id == 'Cacofonix':
    with open('dos_data.json','r') as files:
      data = json.load(files)
      for e in data['Team']:
        if e == 'Rome':
          data['Team'][e][eventType]['Score'] = rome_score
        if e == 'Gual':
          data['Team'][e][eventType]['Score'] = gaul_score
    with open('dos_data.json','w') as fp:
      json.dump(data,fp,indent=4)
  
    with open('dos_data.json','r') as files:
      data = json.load(files)
      dat1 = data['Team']['Gual'][eventType]['Score']
      dat2 = data['Team']['Rome'][eventType]['Score']
    if eventType == "Stone Curling":
      a = data['Clients']
    flag = set()     # creating a set to ignore duplicate port so that notification is passed over to correct clients
    for i in a:
      flag.add(str(i['port']))
    for i in flag:
      print i
      url = "http://127.0.0.1:"+i+"/pushUpdate/Stone Curling/"+rome_score+"/"+gaul_score
      requests.put(url)
    return jsonify({'Gual':dat1},{'Rome':dat2})

  else:
    return "Failure to add Authorization failed"
 
#################Push Update to the clients#########################################
"""
	This is a PUT method which will be called from previous method, that is whenever there is any update in score.
	It takes three argument first is the eventType(Stone Curling) second and third arguments are the score for Rome 
	and Gaul respectively 
"""
@app.route('/pushUpdate/<variable1>/<variable2>/<variable3>',methods=['PUT'])
def sendUpdate(variable1,variable2,variable3):
  print "Message from CACOFONIX"
  print "ROME SCORE--->",variable2
  print "GAUL SCORE--->",variable3
  return "DONE!!!"

#################Registering Clients#########################################
"""
	This is a PUT method which add a client to our database.This is called whenever a client runs fresh.
	In our implementation since we are considering only Stone Curling event hence we are adding to our database 
	clients port and ID (clients subscribed to Stone Curling only)
"""
@app.route('/registerClient/<clientID>/<eventType>/<port>',methods= ['PUT'])
def registerClients(eventType,clientID,port):
  with open('dos_data.json','r') as fp:
    data = json.load(fp)
    data['Clients'].append({'clientID':clientID,'port':port})
  with open('dos_data.json','w+') as files:
    if eventType == "Stone Curling":
      json.dump(data,files,indent=4)
    else:
      print "NOT ADDED"
  return "Success"

def restGetServer(num):
  app.run(threaded=True,port = num)

def restGetServer1():
  app.run(threaded=True)
if __name__ == "__main__":
  app.run(threaded=True,port = 8080)

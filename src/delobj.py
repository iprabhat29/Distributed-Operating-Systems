"""
            This is a function to remove a client off database prevents overcreating of entries in our database file.
"""

import json

def killClient(client,port):
  with open('dos_data.json','r') as files:
    data = json.load(files)
    #print data['Clients'][2]
    data_new = data['Clients']
    #print len(data['Clients'])
    i=0
  while i < len(data['Clients']):
    #print i
    if data['Clients'][i]['clientID'] == client and data['Clients'][i]['port'] == str(port):
      #print type(data['Clients'][i]),i     
      data['Clients'][i].pop('clientID')
      data['Clients'][i].pop('port')
      data['Clients'].pop(i)
      #print data['Clients']
      i=0
      continue
    i=i+1
  with open('dos_data.json','w') as fp:
    json.dump(data,fp,indent=4)

if __name__ == '__main__':
  killClient("Apoorva",5050)

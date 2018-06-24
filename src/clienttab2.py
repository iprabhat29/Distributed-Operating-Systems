
# Contributors:
#    Prabhat Bhatt 
#	Apoorva SAxena

"""
This is Client Anil who is a "Gaulan" and is subscribed to an Event type Stone Curling.
Anil is interested in Gaul medal tally and Roman Medal Tally.He is keeping a close eye on Stone Curling event too.
We are creating a different REST API for Anil which is capable of listening to the score update.
"""

# Import socket module
import socket
import time 
import server
import threading
from thread import *
import restGet
import delobj
def startrest(num):
    restGet.restGetServer(5052)

def Main():
    # local host IP '127.0.0.1'
    host = '127.0.0.1'
 
    # Define the port on which you want to connect
    port = 12345
 
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 
    # connect to server on local computer
    a = s.connect((host,port))
    if a == 0:
      print "Connected"
    # message you send to server
    print "connected!!"
    add_msg = "/registerClient/Anil/Stone Curling/5052"				#ClientID = Anil ; EventType = Stone Curling ; Port = 5050
    s.send(add_msg.encode('ascii'))						#sending registering querry
    data = s.recv(1024)
    message = "/getMedalTally/Rome"						#This client is interested in medal tally of Rome and Gaul.
    message1 = "/getMedalTally/Gual"
    a = 0
    while a<50:									#%0 message with 3 seconds of latency
 
        # message sent to server
        print "Sending Request",a
        s.send(message.encode('ascii'))
        data = s.recv(1024)
        print data
	print "Sending Request",a
        s.send(message1.encode('ascii'))
        data = s.recv(1024)
        print data
        #Adding Latency
        time.sleep(3)										#Here we have given 1 sec break between 2 successive query and maximum query sent by this client is 50
        a= a + 1
    # close the connection
    print "no data..."
    print "closing client"
    delobj.killClient("Anil",5052)
    s.close()
 
if __name__ == '__main__':
  start_new_thread(startrest, (1,))								#starting rest for this client, this is different for server REST.Starting with Port 5051 and localhost
  Main()

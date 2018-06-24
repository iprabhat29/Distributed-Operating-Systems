
# Contributors:
#    Prabhat Bhatt 
#	Apoorva Saxena

"""
This Client Prabhat,who is a "Gaulan" and subscribed to Event type Stone Curling.
Prabhat is interested in Gaul medal tally only.He is keeping a close eye on Stone Curling event
We are creating a different REST API for Prabhat which is capable of listening to the score update.
"""
# Import socket module
import socket
import time 
import server
import threading
from thread import *
import restGet
import delobj

#Starting REST API for this client#
def startrest(num):
  restGet.restGetServer(5050)

#Starting Main segment of the code
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
    add_msg = "/registerClient/Prabhat/Stone Curling/5050"			#ClientID = Apoorva ; EventType = Stone Curling ; Port = 5050
    s.send(add_msg.encode('ascii'))						#sending registering query
    data = s.recv(1024)
    message1 = "/getMedalTally/Gual"						#This client is interested in medal tally of Rome since he is "Gualan"
    a = 0
    while a<50:									#Sending 50 requests to the sever with 2 seconds of delay in between the requests.
        # message sent to server
        print "Sending Request",a
        s.send(message1.encode('ascii'))
        data = s.recv(1024)
        print data
        #Creating Latency 
        time.sleep(2)
        a= a + 1
    # close the connection
    print "no data..."
    print "closing client"
    delobj.killClient("Prabhat",5050)
    s.close()
 
if __name__ == '__main__':
  start_new_thread(startrest, (1,))								#starting rest for this client, this is different for server REST.Starting with Port 5051 and localhost.
  Main()

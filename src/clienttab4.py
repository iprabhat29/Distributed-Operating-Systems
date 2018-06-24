
# Contributors:
#    Prabhat Bhatt 
#	Apoorva SAxena

"""
This is Client Manju who is a Roman she is not subscribed to any event
But she is very much interested in Rome and Gaul medal tally 
We are creating a different REST API for Manju which is capable of listening to the score update.
"""


# Import socket module
import socket
import time 
import server
import threading
from thread import *
import restGet
def startrest(num):
  restGet.restGetServer(5054)

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
    message1 = "/getMedalTally/Rome"				#This client is interested in medal tally of Rome since he is Roman
    message = "/getMedalTally/Gual"				#This client is also interested in medal tally of Gaul

    a = 0
    while a<50:							#50 pairs of requests with 3 seconds of latency 
 
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
        time.sleep(3)
        a= a + 1
    # close the connection
    print "No Data..."
    #time.sleep(20)
    print "closing client"
    s.close()
 
if __name__ == '__main__':
  start_new_thread(startrest, (1,))							#starting rest for this client, this is different for server REST.Starting with Port 5050 and localhost.
  Main()

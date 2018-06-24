
# Contributors:
#    Prabhat Bhatt 
#	Apoorva SAxena

"""
This is Client "Mandvi" who is a "Roman" and subscribed to Event type "Stone Curling".
She is only interested in updated score for stone curling
We are creating a different REST API for "Mandvi" which is capable of listening to the score update.
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
  restGet.restGetServer(5053)

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
    add_msg = "/registerClient/Mandvi/Stone Curling/5053"				#ClientID = Mandvi ; EventType = Stone Curling ; Port = 5053
    s.send(add_msg.encode('ascii'))							#sending registering querry
    data = s.recv(1024)
    #letting the client Sleep snd listen for update
    time.sleep(50)									#Stays asleep fo 50 secs and keep listening for updates
    print "closing client"
    delobj.killClient("Mandvi",5053)							#Removing client from son file
    s.close()
 
if __name__ == '__main__':
  start_new_thread(startrest, (1,))								#starting rest for this client, this is different for server REST.Starting with Port 5053 and localhost
  Main()

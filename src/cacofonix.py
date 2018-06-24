import socket
import time 
import threading
import restGet
from thread import *
from random import randint
def Main():
    # local host IP '127.0.0.1'
    host = '127.0.0.1'
 
    # Define the port on which you want to connect
    port = 12345
 
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 
    # connect to server on local computer
    a = s.connect((host,port))
    # message you send to server
    print "connected!!"
    message = "/incrementMedalTally/Gual/Gold/Cacofonix/"
    message1 = "/incrementMedalTally/Rome/Gold/Cacofonix/"
    #print message3
    a = 0
    while a<50:
        # message sent to server
      print "Sending Request from cacofonix",a
      s.send(message.encode('ascii'))
        # messaga received from server
      data = s.recv(1024)
      print str(data.decode('ascii'))
      print "Sending Second Request from cacofonix",a 
      s.send(message1.encode('ascii'))
      data = s.recv(1024)
      print str(data.decode('ascii'))
      if (a%10 == 0 and a!=0):
        aa = str(randint(1,99))
        bb = str(randint(1,99))
        message3 = "/setScore/Stone Curling/" + aa + "/" + bb + "/Cacofonix"
        print "Sending third request from cacofonix",a
        s.send(message3.encode('ascii'))
        data = s.recv(1024)
        print str(data.decode('ascii'))
        a=a+1
        continue
      time.sleep(2)
      a= a + 1
    # close the connection
    print "no data..."
    #time.sleep(2)
    print "closing client"
    s.close()

def startCacofonix(num):
    Main()
if __name__ == '__main__':
    Main()

"""
    This is the our implementation of Obelix Server it opens socket connection and listens for clients.As soon as the client 
    connects with this server a seperate thread is spawned which opens REST API with port starting with 8080,next thread will 
    start API for new client with port 8081 and so on... 
"""
import socket
from thread import *
import threading
import restGet 
import requests
import re
print_lock = threading.Lock()
#This function creates REST API server for each client which connects
def startserver(num):
  print "RUNNIN SERVER REST--->",num
  restGet.restGetServer(num)
  return

##This is the target thread which is spawned whenever a client connects
def threaded(c,t,c_port,s_port):
    c_port = str(c_port)
    s_port = str(s_port)
    while True:
        data = c.recv(1024)
        #data_url = "http://127.0.0.1:"+s_port+str(data)
        #print "DATA URL-->",data_url
        if not data:
            print('Bye')
            break
        data_temp = re.sub('[^A-Za-z0-9]+', '', data)
        if 'incrementMedalTally' in data_temp:
          url = "http://127.0.0.1:"+s_port+str(data)
          print "Sending Reuest ",url
          data1 = requests.put(url).json()
          c.send(str(data1))
        elif 'getMedalTally' in data_temp:
          url = "http://127.0.0.1:"+s_port+str(data)
          print "Sending Request ",url
          try:
            data1 = requests.get(url).json()
            c.send(str(data1))
          except ValueError:
            print "EXCEPTION"
        elif 'pushUpdate' in data_temp:
          url = "http://127.0.0.1:"+s_port+str(data)
          print "Sending Request ",url
          data1 = requests.put(url)
          c.send(str(data1))
        elif 'setScore' in data_temp:
          url = "http://127.0.0.1:"+s_port+str(data)
          print "Sending request ",url
          data1 = requests.put(url)
          c.send(str(data1))
        elif 'registerClient' in data_temp:
          url = "http://127.0.0.1:"+s_port+str(data)
          print "Sending Request ",url
          data1 = requests.put(url)
          c.send(str(data1))
        elif 'getScore' in data_temp:
          url = "http://127.0.0.1:"+s_port+str(data)
          print "Sending Request ",url
          data1 = requests.get(url).json()
          c.send(str(data1))
    c.close()
 
#listens to client 
def Main():
    host = ""
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to post", port)
    s.listen(5)
    print("socket is listening")
    s_port = 8080
    c_port = 5050
    t=0 
    # a forever loop until client wants to exit
    while True:
 
        # establish connection with client
        c, addr = s.accept()
        print('Connected to :', addr[0], ':', addr[1])
        # Start a new thread for socket communication
        print "Creating Client Threads"
        start_new_thread(startserver, (s_port,))
        # Start a new thread which opens REST API
        print "Creating REST Thread for current client with port ",s_port
        start_new_thread(threaded, (c,t,c_port,s_port))
        t=t+1
        s_port = s_port + 1
        c_port = c_port + 1
    s.close()
 
 
if __name__ == '__main__':
    Main()

# import socket programming library
import socket
 
# import thread module
from thread import *
import threading
import restGet 
import requests
import re
print_lock = threading.Lock()
 
# thread fuction
def startserver(num):
  restGet.restGetServer(num)
  return
def threaded(c,t):
#    print "Acquiring lock for ",addr
#    print_lock.acquire()
#    print "lock acquired"
    while True:
        #print "Acquiring lock for Thread",str(t)
        #print_lock.acquire() 
        #print "lock acquired for Thread",str(t)
      # data received from client
        data = c.recv(1024)
        #print "data received from Thread",str(t)," --> ",data
        #print_lock.release()
        if not data:
            print('Bye')
            break
        data_temp = re.sub('[^A-Za-z0-9]+', '', data)
        #print  data_temp
        if 'incrementMedalTally' in data_temp:
          url = data
          data1 = requests.put(url).json()
          c.send(str(data1))
        elif 'getMedalTally' in data_temp:
          url = data
          print url
          try:
            data1 = requests.get(url).json()
            c.send(str(data1))
          except ValueError:
            print "**************************************************************EXCWPTION"
        elif 'pushUpdate' in data_temp:
          url = data
          data1 = requests.put(url)
          c.send(str(data1))
        elif 'setScore' in data_temp:
          url = data
          data1 = requests.put(url).json()
          c.send(str(data1))
        #print "Releasing lock for Thread",str(t)
        #print_lock.release()
    #print "No data releasing Lock for Thread",str(t)
    #print_lock.release() 
    # connection closed
    c.close()
 
 
def Main():
    host = "" 
    # reverse a port on your computer
    # in our case it is 12345 but it
    # can be anything
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to post", port)
    #restGet.restGetServer() 
    # put the socket into listening mode
    s.listen(5)
    #print("socket is listening")
    port = 8080
    t=0 
    # a forever loop until client wants to exit
    while True:
        # establish connection with client
        print "Socket Is Listening"
        c, addr = s.accept()
        print "Connection Accepted"
        print('Connected To :', addr[0], ':', addr[1])
        # Start a new thread and return its identifier
        print "Creating Client Threads"
        start_new_thread(threaded, (c,t))
        print "C ",c
        print "Creating REST Thread For Current Client With Port ",port
        start_new_thread(startserver, (port,))
        t=t+1
        port = port + 1
    s.close()
 
 
if __name__ == '__main__':
    Main()


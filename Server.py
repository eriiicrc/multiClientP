# -*- coding: utf-8 -*-
#from SocketServer import ThreadingMixIn
from threading import Thread
#import time
import sys
import socket

#Multiclient Python Server: TCP Server Socket Thread Pool

class ClientThread(Thread):

    def __init__(self,addr):
        Thread.__init__(self)
        self.addr=addr
        print >> sys.stderr,"Client whith",addr,"connected"

    def run(self):
        while True:
            data = conn.recv(buff)
            print >> sys.stderr,"Received data:",data
            msg=raw_input("Enter response from Server/Enter close:")
            if msg=="close":
                break
            conn.send(msg)#echo

#Multithreaded Python Server: TCP Server Socket Programm Stub

#inicializating variables
ip="localhost"
port=2222
buff=1024
addr=(ip,port)
#creating socket
stcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
stcp.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
stcp.bind(addr)

tclients=[]

while True:
    stcp.listen(4)
    print >>sys.stderr,"...Waiting for connections..."
    (conn,(ip,port))=stcp.accept()
    newthread=ClientThread((ip,port))
    newthread.start()
    tclients.append(newthread)

for t in tclients:
    t.join()









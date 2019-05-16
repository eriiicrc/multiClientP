# -*- coding: utf-8 -*-
import socket
import sys
import time

host="localhost";
port=2222
buff=1024

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((host,port))

if sock.connect((host,port)):
    print>>sys.stderr,"..Connecting to Server.."
    time.wait(0.1)
nick=raw_input("Choose Nick:")
msg=raw_input(nick+":")
while msg!="close":
    sock.send(msg)
    data = sock.recv(buff)
    print>>sys.stderr,"Received data:"
    msg=raw_input(nick+":")
print>>sys.stderr,"Bye"
sock.close()



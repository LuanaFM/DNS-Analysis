#!/usr/bin/python2
import socket, sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("200.160.2.3",43))
try:
    s.send(sys.argv[1]+'\r\n')
    res = s.recv(1024)
    print(res)
except Exception as error:

    print ("Falha:"+ str(error))


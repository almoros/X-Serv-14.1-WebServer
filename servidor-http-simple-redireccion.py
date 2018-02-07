#!/usr/bin/python3

"""
Simple HTTP Server
Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
"""

import socket

# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 1233))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(1)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an infinite loop)

while True:
    print('Waiting for connections')
    (recvSocket, address) = mySocket.accept()
    print('HTTP request received:')
    print(recvSocket.recv(1024))
    recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
		    "<head><meta http-equiv='Refresh' content=0;url=https://github.com/CursosWeb></head>" +
                    "<html><body><h1>Redirigiendo a 'CursosWeb" +
		    "</h1></body></html>" +
                    "\r\n", 'utf-8'))
recvSocket.close()

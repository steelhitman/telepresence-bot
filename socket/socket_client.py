#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = '192.168.100.14' # Get local machine name
port = 1234                # Reserve a port for your service.

s.connect((host, port))
print s.recv(1024)
inp=raw_input("Enter data to send: ")
s.send(inp)
                    		# Close the socket when done
print s.recv(1024)
inp=raw_input("Enter data to send: ")
s.send(inp)
s.close                     # Close the socket when done
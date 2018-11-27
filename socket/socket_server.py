#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
import serial 
s = socket.socket()         # Create a socket object
#host = socket.gethostname() # Get local machine name
host='192.168.100.13'
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   #ser = serial.Serial('/dev/ttyACM0', 9600)
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   #c.send('Connected')
   data= c.recv(1024)
   print data
   #ser.write(data)
   #incomming=ser.inWaiting()
   #print incomming
   incomming=1
   if incomming!=0:
   		wait=1
   else:
   	    wait=0
   if wait==1:
   		#c.send(ser.readline())
   		c.send("Left Collision")
   #ser.close()
   c.close()                # Close the connection
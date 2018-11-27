import serial
ser=serial.Serial('COM11',9600)
while 1:
	val=raw_input("Enter 1:")
	ser.write(val)
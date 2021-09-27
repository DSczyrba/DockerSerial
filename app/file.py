import serial
import time

while True:
    try:
        serialPort = serial.Serial(port = "/dev/virtual1", baudrate=115200,
                                bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
        print(serialPort)
        break
    except:
        print("Port nicht vorhanden...")
        time.sleep(3)
    
while(1):
    if(serialPort.in_waiting > 0):
        serialString = serialPort.readline()
        print(serialString.decode('ASCII').replace("\n", ""))
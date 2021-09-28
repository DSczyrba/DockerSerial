import serial.tools.list_ports
import re
import socket
import subprocess
import os
import time


check_for = "Silicon"


for x in [[x, y] for x, y, _ in sorted(serial.tools.list_ports.comports())]:
    try:
        re.search(check_for, x[1]).group()
        found_port = x[0]
        break
    except AttributeError:
        pass

print("Gefundener Port:", found_port)
print(socket.gethostbyname(socket.gethostname()))

command = f"com2tcp.exe --telnet --ignore-dsr --baud 115200 \\\\.\\{found_port} 23"
print(command)

subprocess.Popen(command)
subprocess.run("docker build -t lscheibe/dockerserial:dev .")

command = f"docker run -d --name dockerserial -p 5080:5080 -e IP_ADRESS={socket.gethostbyname(socket.gethostname())} lscheibe/dockerserial:dev"
print(command)
subprocess.run(command)

print("Wir kommen hier an...")

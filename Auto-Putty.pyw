import serial.tools.list_ports
import subprocess
import time
from tkinter import simpledialog

def check_ports():
    ports = serial.tools.list_ports.comports()
    new_ports = []
    disconnected_ports = []
    current_ports = set([port.device for port in ports])  # Get the current set of ports

    # Check for new ports
    for port, desc, hwid in sorted(ports):
        if port not in existing_ports:
            new_ports.append(port)
            existing_ports.add(port)  # Add the new port to existing_ports
            return port

    # Check for disconnected ports
    ports_to_remove = []
    for port in existing_ports:
        if port not in current_ports:
            disconnected_ports.append(port)
            ports_to_remove.append(port)  # Store the port to be removed

    # Remove disconnected ports from existing_ports
    for port in ports_to_remove:
        existing_ports.remove(port)

    return None

def open_putty(com_port, baud_rate):
    subprocess.Popen(['putty.exe', '-serial', com_port, '-sercfg', f'{baud_rate},8,n,1,N'])


existing_ports = set([port.device for port in serial.tools.list_ports.comports()])

while True:
    com_port = check_ports()
    if com_port:
        baud_rate = simpledialog.askstring("auto putty", "New serial port detected. Enter baud rate:")
        if baud_rate:
            print(baud_rate)
            print(com_port)
            open_putty(com_port, baud_rate)
        com_port = None
    time.sleep(1)
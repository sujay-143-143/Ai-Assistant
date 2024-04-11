import serial
from time import sleep

# Define serial port settings
SERIAL_PORT = 'COM3'  # Change this to the port your Arduino is connected to
BAUD_RATE = 9600

# Create serial connection
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

# Function to send command to turn on the relay
def turn_relay_on():
    ser.write(b'1')
    print("Relay turned on")

# Function to send command to turn off the relay
def turn_relay_off():
    ser.write(b'0')
    print("Relay turned off")



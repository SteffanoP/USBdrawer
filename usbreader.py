import serial

ser = serial.Serial(port='COM3', \
        baudrate=9600,\
        parity=serial.PARITY_NONE,\
        stopbits=serial.STOPBITS_ONE,\
        bytesize=serial.EIGHTBITS,\
        timeout=1)

#Debug das entradas do teclado
try:
    _input = raw_input
except NameError:
    _input = input

def start() :
    print("What is the port?")
    port = input()
    print("Running on: " + ser.name)

#Início do programa
while True :
    start();
    x = ser.read(28)
    print("Data on the port")
    print(x)

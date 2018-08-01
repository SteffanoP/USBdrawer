import serial

#Debug das entradas do teclado
try:
    _input = raw_input
except NameError:
    _input = input

def start() :
    print ("Qual é a porta?(COM1 - COM16)")
    port = input() #Port input
    print ("Qual é o baudrate?")
    baudrate = input() #baudrate input
    ser = serial.Serial(port=port, \
            baudrate=baudrate,\
            parity=serial.PARITY_NONE,\
            stopbits=serial.STOPBITS_ONE,\
            bytesize=serial.EIGHTBITS,\
            timeout=4) #Serial Settings
    print("Porta: " + ser.name) #Print the input port
    global data
    data = ser.read(28) #Reads the data and it length

#Start
start();
while (data != 0) :
    print(data)

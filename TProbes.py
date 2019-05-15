import pyserial

class TemperatureProbes:
    def __init__(self, n, baud):
        self.baud = baud
        if (n==0):
            self.port = '/dev/ttyACM0'
        elif (n==1):
            self.port = '/dev/ttyACM1'
        elif (n==2):
            self.port = '/dev/ttyACM2'
        elif (n==3):
            self.port = '/dev/ttyACM3'
        else:
            print("Invalid ending")
            exit
        
     #Prints Port name and Baud rate, in case you forgot
    def whosmans(self):
        print("Port name is " + self.port)
        print("Baud Rate is " + str(self.baud))

    #Prints method names and description
    def helpme(self):
        methods = ["whosmans", "changeP ", "changeB ", "openC   ", "line    "]
        inputs = ["N/A              ", "N/A              ", "New Baud Rate (int)", "N/A              ", "N/A              ",]
        desc = ["Output port name and baud rate.", "Change port name", "Change baud rate", "Open serial port for probe", "Gets serial output data"]
        
        for i in range(4):
            print(methods[i] + '    ' + inputs[i] + '    ' + desc[i])
        
    #Change port name
    def changeP(self, n):
        if (n==0):
            self.port = '/dev/ttyACM0'
        elif (n==1):
            self.port = '/dev/ttyACM1'
        elif (n==2):
            self.port = '/dev/ttyACM2'
        elif (n==3):
            self.port = '/dev/ttyACM3'
        else:
            print("Invalid ending")
            exit

    #Change Baud Rate 
    def changeB(self, Nbaud):
        self.baud = Nbaud

    #opens serial port for conductivity probe
    def openC(self):
        fprintf("Trying %s.\n", self.port)
        ser = serial.Serial(self.port, self.baud)
        fprintf("Connected to %s.\n", self.port)
        print("Closing...just in case")
        ser.close()
        print("Opening again")
        ser.open()
        print("yeet")
        
    def line(self):
        line = ser.readline().strip().decode('utf-8')
        

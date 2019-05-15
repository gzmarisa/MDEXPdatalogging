import serial

class TemperatureProbes:

    def __init__(self, baud):
        self.port = str(input('What is the port name?   '))
        self.baud = baud

#Prints Port name and Baud rate, in case you forgot
    def whosmans(self):
        print("Port name is " + self.port)
        print("\n Baud Rate is " + str(self.baud))

    #Prints method names and description
    def helpme(self):
        methods = ["whosmans", "changeP ", "changeB ", "openC   "]
        inputs = ["N/A              ", "N/A              ", "New Baud Rate (int)", "N/A              "]
        desc = ["Output port name and baud rate.", "Change port name", "Change baud rate", "Open serial port for probe"]
        
        for i in range(4):
            print(methods[i] + '    ' + inputs[i] + '    ' + desc[i])
        
    #Change port name
    def changeP(self):
        self.port = str(input('What is the port name?   '))

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
        

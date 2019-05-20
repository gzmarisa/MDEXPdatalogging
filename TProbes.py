import serial

class TemperatureProbes:
    def fprintf(stream, format_spec, *args):
        stream.write(format_spec % args)
        
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
        print("T Port name is " + self.port)
        print("T Baud Rate is " + str(self.baud))

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
        #print("Trying " + self.port)
        self.ser = serial.Serial(self.port, self.baud)
        #print("Closing...just in case")
        self.ser.close()
        #print("Opening again")
        print("Temp. Probes are connected to " + self.port)
        self.ser.open()
        #print("yeet")
        l = self.ser.readline().strip().decode('utf-8')        
    def line(self):
        return self.ser.readline().strip().decode('utf-8')



        

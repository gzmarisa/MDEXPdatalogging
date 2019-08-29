import serial

class TemperatureProbes:        
    def __init__(self, n, baud):
        self.baud = baud
        if (n==0):
            self.port = "COM0"
        elif (n==1):
            self.port = "COM1"
        elif (n==2):
            self.port = "COM2"
        elif (n==3):
            self.port = "COM3"
        elif (n==4):
            self.port = "COM4"
        elif (n==5):
            self.port = "COM5"
        elif (n==6):
            self.port = "COM6" 
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
            self.port = "COM0"
        elif (n==1):
            self.port = "COM1"
        elif (n==2):
            self.port = "COM2"
        elif (n==3):
            self.port = "COM3"
        elif (n==4):
            self.port = "COM4"
        elif (n==5):
            self.port = "COM5"
        elif (n==6):
            self.port = "COM6"  
        else:
            print("Invalid ending")
            exit

    #Change Baud Rate 
    def changeB(self, Nbaud):
        self.baud = Nbaud

    #opens serial port for Temperature Probes
    def openC(self):
        print("Trying " + self.port + " at " + str(self.baud) + " baud")
        try:
            self.ser = serial.Serial(
                port=self.port,
                baudrate=self.baud,
                timeout=0.5
            )
        except:
            print("couldn't create serial port")
            pass
        #print("Closing...just in case")
        self.ser.close()
        #print("Opening again")
        self.ser.open()
        #print("yeet")
        print("Conductivity Probe is connected to " + self.port)
        #l = self.ser.readline().strip().decode('utf-8')
        #print("Successfully read a line from the serial port")
        #print(l)
        
    def line(self):
         n = self.ser.readline().strip().decode('utf-8')
         self.ser.flushInput()
         return n
    
    def flushh(self):
        self.ser.flushInput()

    def getLineIfAvailable(self):
        if self.ser.in_waiting:
            line = self.ser.readline().decode('utf-8')
            return line
        return None

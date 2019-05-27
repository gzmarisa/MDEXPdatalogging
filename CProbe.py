import serial

class ConductivityProbe:
    
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
        print("C Port name is " + self.port)
        print("C Baud Rate is " + str(self.baud))

    #Prints method names and description
    def helpme(self):
        # Define these inside the class, but outside the function for maximum efficiency
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
        l = self.ser.readline().strip().decode('utf-8')
        #print("Successfully read a line from the serial port")
        #print(l)
        
    def line(self):
        while not(self.ser.in_waiting):
            pass
            
        return self.ser.readline().strip().decode('utf-8')
        

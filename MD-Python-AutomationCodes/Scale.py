import serial
import sys
import time as t
import datetime

class Scale:
    def fprintf(stream, format_spec, *args):
        stream.write(format_spec % args)
    def __init__(self, n, baud):
        self.baud = baud
        #This will only work on this code
##        if (isinstance(n,int) == True):
##            self.port = "/dev/ttyUSB" + str(n)
##        else:
##            raise Exception('Invalid serial port ending: must be 1 or 2 digit integer')
        if (n==0):
            self.port = "/dev/ttyUSB0"
        elif (n==1):
            self.port = "/dev/ttyUSB1"
        elif (n==2):
            self.port = "/dev/ttyUSB2"
        elif (n==3):
            self.port = "/dev/ttyUSB3"
        else:
            print("Invalid ending")
            exit

    #Prints Port name and Baud rate, in case you forgot
    def whosmans(self):
        print("S Port name is " + self.port)
        print("S Baud Rate is " + str(self.baud))

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
            self.port = "/dev/ttyUSB0"
        elif (n==1):
            self.port = "/dev/ttyUSB1"
        elif (n==2):
            self.port = "/dev/ttyUSB2"
        elif (n==3):
            self.port = "/dev/ttyUSB3"
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
        l = self.ser.readline().strip().rpartition(b' g')[0].decode('utf-8')
        #print("Successfully read a line from the serial port")
        #print(l)

    def line(self):
        n = 0
        c = datetime.datetime.now()
        sec = c.second
        if (sec%5 == 0) and (c.microsecond < 100):
            n = self.ser.readline().strip().rpartition(b' g')[0].decode('utf-8')
        return n

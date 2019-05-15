class ConductivityProbe:
  def __init__(self, port, baud):
    self.port = str(port)
    self.baud = baud

    #Prints Port name and Baud rate, in case you forgot
    def whosmans(self):
        print("Port name is " + self.port)
        print("\n Baud Rate is " + self.baud)

    #Change port name
    def changeP(self, Nport):
        self.port = Nport

    #Change Baud Rate
    def changeB(self, Nbaud):
        self.baud = Nbaud

    #opens serial port for conductivity probe
    def openC(self):
        #fprintf("Trying %s", self.port)
        ser1 = serial.Serial(self.port, self.baud)
        #print("Connected to ACM2")
        #print("Closing Ser1 just in case")
        ser1.close()
        #print("Opening Ser1 because, um,  duh...")
        ser1.open()


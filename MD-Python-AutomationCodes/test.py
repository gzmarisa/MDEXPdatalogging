##import serial
##print("Cond", "Weight","HotIn", "HotOut", "ColdIn","ColdOut","Month","Day","Hour","Minute","Second",sep='\t')
####
#####print("Trying " + self.port + " at " + str(self.baud) + " baud")
####print("trying")
####ser = serial.Serial('/dev/ttyACM1',115200)
####    #timeout=0.5
####    #print("couldn't create serial port")
####    #pass
####print("Closing...just in case")
####ser.close()
####print("Opening again")
####ser.open()
####print("yeet")
#####print("Conductivity Probe is connected to " + self.port)
####print("connected")
####l = ser.readline().strip().decode('utf-8')
####print("Successfully read a line from the serial port")
####print(l)
#####return self.ser.readline().strip().split('\t').decode('utf-8')
####print(type(l))
####f = [4]
#####print(type(f[1]))
####f = l.split('\t')
####n = []
####for i in range(0, 4):
####    n.append(float(f[i]))
####    print(i)
####print(n)
##

##for i in range(1, 300):
##    m = i/60
##    #print(m)
##    #print(1%(i/60))
##    #if (1%(i/60)):
##    #    print('wooooopoiryhgnbj;erdsfg;olewjs')
##    if (1%m == 0):
##        print('git')
##        print(i)
##        print(m)
##    i = i+1
##
##if(5/1 == 0) == True:
##    print("asdkfj")
##m = []
##m.append(6)
##print(m[0])
import sys
import time as t
import datetime
from CProbe import ConductivityProbe
from TProbes import TemperatureProbes
from Scale import Scale
import serial
##con = ConductivityProbe(3, 115200)
##con.openC()
##T = TemperatureProbes(2, 115200)
##T.openC()
##S = Scale(0, 19200)
##S.openC()
##print("TIME\t\tConductivity\t Weight\t\tTemps")
##i = 0
##while(i != 600):
##    d = datetime.date.today()
##    c = datetime.datetime.now()
##    print(str(c), con.line(), S.line(), T.line(), sep='\t')
##    i = i+1
##    #t.sleep(1)
port = "/dev/ttyUSB1"
baud = 19200
ser = 0
print("Trying " + port + " at " + str(baud) + " baud")
ser = serial.Serial(
    port=port,
    baudrate=baud,
    timeout=0.5
)
##except:
##    print("couldn't create serial port")
##    pass
##    #print("Closing...just in case")
ser.close()
print("Opening again")
ser.open()
print("yeet")
print("Conductivity Probe is connected to " + port)
l = ser.readline().strip().rpartition(b' g')[0].decode('utf-8')
print("eiuyfghwealifuyh")
#while not(ser.inWaiting()):  # Or: while ser.inWaiting():
i = 0
j = 0
while i != 1200000:
    n = 0
    c = datetime.datetime.now()
    sec = c.second
    m = 0
    o = ""
    if (sec%5 == 0):    # and (c.microsecond < 100):
        n = ser.readline().strip().rpartition(b' g')[0].decode('utf-8')
        print(n)
##        if len(n) != 0:
##            o = ""
##            while j != len(n)-1:
##                m =  ord(n.index(j))
##                o = str(m) + o
##                j = j+1
        print("yeeee")
        #print(sec)
        #print(o)
    else:
        n = n
    #print(n)
    #print("help")
    i = i+1
    #print(i)


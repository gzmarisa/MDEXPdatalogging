import sys
import time as t
from time import sleep
import datetime
from CProbe import ConductivityProbe
from TProbes import TemperatureProbes
from Scale import Scale

# Request Sensor Ports/Connection info
C = ConductivityProbe(1, 115200)
C.openC()

T = TemperatureProbes(0, 115200)
T.openC()

S = Scale(0, 19200)
S.openC()

# Request File Name
filename = str(input("What would you like the file name to be?   ")) + ".csv"
file = open(filename, "w+")
print("Opened file")
file.write("DISCLAIMER: This software is experimental. Use at your own risk. Sensor data is NOT synchronized.\n")
print("DISCLAIMER: This software is experimental. Use at your own risk. Sensor data is NOT synchronized.\n")
file.close()
print("Closed file")

# Tell the scale to start sending stuff once per second.
S.start()

while (True):
    #Get current date and time
    #currentDate = datetime.date.today()
    #currentDate = currentDateTime
    currentDateTime = datetime.datetime.now()

    #Check for Temp Sensors, Conductivty Sensors, Scale
    tempC = C.getLineIfAvailable()
    tempS = S.getLineIfAvailable()
    tempT = T.getLineIfAvailable()

    if (tempC is None) and (tempS is None) and (tempT is None):
        sleep(0.5)    
        continue

    file = open(filename, "a+")
    # TODO: 
    print(currentDateTime, end='\n')
    file.write(str(currentDateTime)+'\n')

    if not (tempC is None):
        print('C: ',tempC, sep='\t', end='')
        file.write('C: ' + tempC)

    if not (tempS is None):
        print('S: ',tempS, sep='\t', end='')
        file.write('S: ' + tempS)

    if not (tempT is None):
        print('T: ',tempT, sep='\t', end='')
        file.write('T: ' + tempT)
    print('\n')
    file.flush()
    file.close()

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

#Request File name for raw conductivty data
filenameConductivity = str(input("What would you like the file name for the raw conductivity data to be?   ")) + ".csv"
fileConductivity = open(filenameConductivity, "w+")
print("Opened Conductivity file")
fileScale.close()
print("Closed Conductivity file")


#Request File name for raw temperature data
filenameTemperature = str(input("What would you like the file name for the raw temperature data to be?   ")) + ".csv"
fileTemperature = open(filenameTemperature, "w+")
print("Opened Temperature file")
fileScale.close()
print("Closed Temperature file")

# Request File Name for raw scale data
filenameScale = str(input("What would you like the file name for the raw scale data to be?   ")) + ".csv"
fileScale = open(filenameScale, "w+")
print("Opened Scale file")
fileScale.close()
print("Closed Scale file")

#Create arrays for the different sensors 
interval = 59
conductivityArray = [None]*interval
temperatureArray = [None]*interval
scaleArray = [None]*interval

# Tell the scale to start sending stuff once per second.
S.start()

while (True):
    #Get current date and time
    #currentDate = datetime.date.today()
    #currentDate = currentDateTime
    currentDateTime = datetime.datetime.now()

    #Check for Temp Sensors, Conductivty Sensors, Scale
    tempC = C.getLineIfAvailable()
    tempT = T.getLineIfAvailable()
    tempS = S.getLineIfAvailable()

    if (tempC is None) and (tempT is None) and (tempS is None):
        sleep(0.05)    
        continue

    #file = open(filename, "a+")
    #open the raw data files 
    fileConductivity = open(filenameConductivity, "a+")
    fileTemperature = open(filenameTemperature, "a+")
    fileScale = open(filenameScale, "a+")
    
    print(currentDateTime, end='\n')
    fileConductivity.write(str(currentDateTime)+'\n')
    fileTemperature.write(str(currentDateTime)+'\n')
    fileScale.write(str(currentDateTime)+'\n')

    if not (tempC is None):
        print(tempC, sep='\t', end='')
        fileConductivity.write(tempC)
    print('\n')
    fileConductivity.flush()
    fileConductivity.close()   

    if not (tempT is None):
        print(tempT, sep='\t', end='')
        fileTemperature.write(tempT)
    print('\n')
    fileTemperature.flush()
    fileTemperature.close()
        
    if not (tempS is None):
        print(tempS, sep='\t', end='')
        fileScale.write(tempS)    
    print('\n')
    fileScale.flush()
    fileScale.close()

#! /bin/python3
import sys
import time as t
from time import sleep
import datetime
from CProbe import ConductivityProbe
from TProbes import TemperatureProbes
from Scale import Scale

C = ConductivityProbe(6, 115200)
C.openC()


S = Scale(4, 19200)
S.openC()

T = TemperatureProbes(3, 115200)
T.openC()






filename = str(input("What would you like the file name to be?   ")) + ".csv"
file = open(filename, "w+")
#print("Opened file")
file.write("DISCLAIMER: This software is experimental. Use at your own risk. Sensor data is NOT synchronized.\n")
print("DISCLAIMER: This software is experimental. Use at your own risk. Sensor data is NOT synchronized.\n")
file.close()
#print("Closed file")

# Tell the scale to start sending stuff once per second.
S.start()

# Clear the input buffers so we don't get a huge data dump?
C.clear()
S.clear()
T.clear()

c_count = 0
s_count = 0
t_count = 0

try:
    while (True):
        #Get current date and time
        #currentDate = datetime.date.today()
        currentDateTime = datetime.datetime.now()

        tempC = C.getLineIfAvailable()
        tempS = S.getLineIfAvailable()
        tempT = T.getLineIfAvailable()
        
        

        if (tempC is None) and (tempS is None) and (tempT is None):
            sleep(0.001)    
            continue

        with open(filename, "a+") as file:
            
            print(currentDateTime, end='\n')
            file.write(str(currentDateTime)+'\n')
            
            if not (tempC is None):
                print('C: ',tempC, sep='\t', end='')
                file.write('C: ' + tempC)
                c_count += 1

            if not (tempS is None):
                print('S: ',tempS, sep='\t', end='')
                file.write('S: ' + tempS)
                s_count += 1

            if not (tempT is None):
                print('T: ',tempT, sep='\t', end='')
                file.write('T: ' + tempT)
                t_count += 1
                
            print('\n')
            
            
except KeyboardInterrupt:
    pass

print('Counts: C = {}, S: {}, T: {}\n'.format(c_count, s_count, t_count))

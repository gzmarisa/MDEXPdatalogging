#! /bin/python3
import sys
import time as t
import datetime
from CProbe import ConductivityProbe
from TProbes import TemperatureProbes
from Scale import Scale

con = ConductivityProbe(1, 115200)
con.openC()

T = TemperatureProbes(0, 115200)
T.openC()

S = Scale(0, 19200)
S.openC()


exitWeight = str(input("At what distillate weight would you like the program to end?   "))

filename = str(input("What would you like the file name to be?   ")) + ".csv"
f = open(filename, "w+")
print("Opened file")
f.write("DISCLAIMER: This software is experimental. Use at your own risk. Sensor data is NOT synchronized.\n")
print("DISCLAIMER: This software is experimental. Use at your own risk. Sensor data is NOT synchronized.\n")
f.close()
print("Closed file")

# Tell the scale to start sending stuff once per second.
S.start()

month = []
day = []
hour = []
minute = []
second = []
cond = []
wt = []
temp = []
i = 0
m = float(0)
e = 0
dd = 0
n = 0


d = datetime.date.today()
c = datetime.datetime.now()

conn=con.line()
weight=S.line()
temps=T.line()
print(conn, weight, temps, mo, dayy, h, mi, sec, sep='\t')

while (True):
        #Get current date and time
        d = datetime.date.today()
        c = datetime.datetime.now()
        h = c.hour
        mi = c.minute
        sec = c.second
        dayy = d.day
        mo = d.month
        if (c.microsecond < 1000):
            tempC = con.line()
            tempS = S.line()
            tempT = T.line()
            if (tempC!= conn and tempC!="" and tempC!=None):
                conn = tempC
            if (tempS!= weight and tempS!="" and tempS!=None):
                weight = tempS
            if (tempT!= temps and tempT!="" and tempT!=None):
                temps = tempT     
        if (sec == 0) and (m % saveInterval == 0) and (c.microsecond < 1000):
            conn=con.line()
            temps=T.line()
            print(conn, weight, temps, mo, dayy, h, mi, sec, sep='\t')
            S.flushh()
            f=open(filename, "a+")
            f.write(str(conn)  + "\t" + str(weight) + "\t" + temps + "\t" + str(mo) + "\t" + str(dayy) + "\t" + str(h) + "\t" + str(mi) + "\t" + str(sec) + "\n")
            f.close()
            n = n+1
            S.flushh()
        elif (sec == 0) and (m % printInterval == 0) and (c.microsecond < 1000):
            conn=con.line()
            temps=T.line()
            print(conn, weight, temps, mo, dayy, h, mi, sec, sep='\t')
            S.flushh()

        else:
            pass
            
        if (sec == 0) and (c.microsecond < 100):
            m = m+1
        if (weight >= exitWeight):
            break


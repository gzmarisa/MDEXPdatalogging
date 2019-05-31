#! /bin/python3
import sys
import time as t
import datetime
from CProbe import ConductivityProbe
from TProbes import TemperatureProbes
from Scale import Scale

#def fprintf(stream, format_spec, *args):
    #stream.write(format_spec % args)

#def main():
    
con = ConductivityProbe(1, 115200)
#Testing methods
#con.whosmans()
#con.helpme()
#con.changeB(80000)
#con.changeP(1)
#con.whosmans()
con.openC()
#l = con.line()
#+-print(l)

T = TemperatureProbes(0, 115200)
#Testing methods
#T.whosmans()
#T.helpme()
#T.changeB(80000)
#T.changeP(0)
#T.whosmans()
T.openC()
#l = T.line()
#print(l)

S = Scale(1, 19200)
#Testing methods
#S.whosmans()
#S.helpme()
#S.changeB(80000)
#S.changeP(7)
#S.whosmans()
S.openC()
#l = S.line()
#print(l)

printInterval = float(input("What interval (in minutes) would you like the data to be printed?"))
#print(type(printInterval))


saveInterval = float(input("What interval (in minutes) would you like the data to be saved to a text file?"))

filename = str(input("What would you like the file name to be?"))
f = open(filename, "w+")
print("Opened file")
f.write("Cond\tWeight\tHotIn\tHotOut\tColdIn\tColdOut\tMonth\tDay\tHour\tMinute\tSecond\n")
print("saved first line to file")
f.close()
print("Closed file")

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

print("Waiting for seconds to equal 0")
time = t.localtime(None).tm_sec
while(time != 0):
    time = t.localtime(None).tm_sec            

print("Cond", "Weight","HotIn", "HotOut", "ColdIn","ColdOut","Month","Day","Hour","Minute","Second",sep='\t')
d = datetime.date.today()
c = datetime.datetime.now()
h = c.hour
mi = c.minute
sec = c.second
dayy = d.day
mo = d.month
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
            temp = S.line()
            if (temp!= weight and temp!="" and temp!=None):
                weight=temp
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


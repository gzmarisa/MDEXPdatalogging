#! /bin/python3
import sys
import time as t
import datetime
from CProbe import ConductivityProbe
from TProbes import TemperatureProbes
from Scale import Scale

    
con = ConductivityProbe(0, 115200)
con.openC()

T = TemperatureProbes(1, 115200)
T.openC()


S = Scale(0, 19200)
S.openC()

printInterval = int(input("What interval (in minutes) would you like the data to be printed?   "))
saveInterval = int(input("What interval (in minutes) would you like the data to be saved to a text file?   "))
filename = str(input("What would you like the file name to be?"))

f = open(filename, "w+")
print("Opened file")
f.write("Cond\tWeight\tHotIn\tHotOut\tColdIn\tColdOut\tMonth\tDay\tHour\tMinute\tSecond\n")
print("saved first line to file")
f.close()
print("Closed file")

month = []
dayy = []
hour = []
minute = []
second = []
cond = []
wt = []
temp = []
i = 0
m = 0
e = 0
dd = 0
n = 0
m = float(0)

print("Waiting for seconds to equal 0")
time = t.localtime(None).tm_sec
    #loop for making the code start when seconds = 0
while(time != 0):
    #print("Waiting for seconds to equal 0")
    time = t.localtime(None).tm_sec            

print("Cond", "Weight","HotIn", "HotOut", "ColdIn","ColdOut","Month","Day","Hour","Minute","Second",sep='\t')
d = datetime.date.today()
c = datetime.datetime.now()

month.append(d.month)
dayy.append(d.day)
hour.append(c.hour)
minute.append(c.minute)
second.append(c.second)
cond.append(con.line())
#print("got conductivity")
wt.append(S.line())
#print("got weight")
temp.append(T.line())
f=open(filename, "a+")
f.write(str(cond[n])  + "\t" + str(wt[n]) + "\t" + temp[n] + "\t" + str(month[n]) + "\t" + str(dayy[n]) + "\t" + str(hour[n]) + "\t" + str(minute[n]) + "\t" + str(second[n]) + "\n")
f.close()
print(cond[n], wt[n], temp[n], month[n], dayy[n], hour[n], minute[n], second[n], sep='\t')
n = n+1
m = m+1

while (True):
    #print("I'm alive, I swear. Just don't ask me to complete a CAPTCHA")
    d = datetime.date.today()
    c = datetime.datetime.now()
    h = c.hour
    mi = c.minute
    sec = c.second
    da = d.day
    mo = d.month
    
    #print("m % printInterval " + str(m % printInterval))
    if (sec == 0) and (m % saveInterval == 0) and (c.microsecond < 1000):
        #print("Case 1")
        month.append(d.month)
        dayy.append(d.day)
        hour.append(c.hour)
        minute.append(c.minute)
        second.append(c.second)
        cond.append(con.line())
        #print("got conductivity")
        wt.append(S.line())
        #print("got weight")
        temp.append(T.line())
        f=open(filename, "a+")
        f.write(str(cond[n])  + "\t" + str(wt[n]) + "\t" + temp[n] + "\t" + str(month[n]) + "\t" + str(dayy[n]) + "\t" + str(hour[n]) + "\t" + str(minute[n]) + "\t" + str(second[n]) + "\n")
        f.close()
        print(cond[n], wt[n], temp[n], month[n], dayy[n], hour[n], minute[n], second[n], sep='\t')
        n = n+1
        #print(m)
    elif  (sec == 0) and (m % printInterval == 0) and (c.microsecond <1000):
        #print("Case 2")
        conn = con.line()
        #print("got conductivity")
        weight = S.line()
        #print("got weight")
        temps = T.line()
        #print(m)
        print(conn, weight, temps, str(mo), str(da), str(h), str(mi), str(sec), sep='\t')
    else:
        pass    
        
    if (sec == 0) and (c.microsecond < 100):
        m = m+1

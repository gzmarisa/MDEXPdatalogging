#! /bin/python3
import sys
import time as t
import datetime


printInterval = 1
print(type(printInterval))
print("printInterval = " + str(printInterval))
printInterval = float(1)
print(type(printInterval))
print("printInterval = " + str(printInterval))

saveInterval = 5
print(type(printInterval))
saveInterval = float(5)
print(type(printInterval))

filename ="test.txt"
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
tes = []
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
    #print(t.localtime(None))
    #print("Still kickin")
print("seconds == 0, bitch")

print("Cond", "Weight","HotIn", "HotOut", "ColdIn","ColdOut","Month","Day","Hour","Minute","Second",sep='\t')
d = datetime.date.today()
c = datetime.datetime.now()
#print(d)
#print(c)
month.append(d.month)
dayy.append(d.day)
hour.append(c.hour)
minute.append(c.minute)
second.append(c.second)
cond.append("ye")
wt.append("no")
tes.append("yeeyee")
f=open(filename, "a+")
f.write(str(cond[n])  + "\t" + str(wt[n]) + "\t" + tes[n] + "\t" + str(month[n]) + "\t" + str(dayy[n]) + "\t" + str(hour[n]) + "\t" + str(minute[n]) + "\t" + str(second[n]) + "\n")
f.close()
print(cond[n], wt[n], tes[n], month[n], dayy[n], hour[n], minute[n], second[n], sep='\t')
n = n+1
m = m+1
while (True):
    d = datetime.date.today()
    c = datetime.datetime.now()
    h = c.hour
    mi = c.minute
    sec = c.second
    da = d.day
    mo = d.month
    #print("sec = " + str(sec) + "micro = " + str(c.microsecond))
    #print("m % saveInterval " + str(m % saveInterval))
    #print("m % printInterval " + str(m % printInterval))
    if (sec == 0) and (m % saveInterval == 0) and (c.microsecond < 1000):
        print("Case 1")
        month.append(d.month)
        dayy.append(d.day)
        hour.append(c.hour)
        minute.append(c.minute)
        second.append(c.second)
        cond.append("ye")
        wt.append("no")
        tes.append("yeeyee")
        f=open(filename, "a+")
        f.write(str(cond[n])  + "\t" + str(wt[n]) + "\t" + tes[n] + "\t" + str(month[n]) + "\t" + str(dayy[n]) + "\t" + str(hour[n]) + "\t" + str(minute[n]) + "\t" + str(second[n]) + "\n")
        f.close()
        print(cond[n], wt[n], tes[n], month[n], dayy[n], hour[n], minute[n], second[n], sep='\t')
        n = n+1
        print(m)
    elif  (sec == 0) and (m % printInterval == 0) and (c.microsecond <1000):
        print("Case 2")
        conn = "skjhfi"
        weight = "sde"
        temps = "sefjnwsejf"
        
        print(conn, weight, temps, str(mo), str(da), str(h), str(mi), str(sec), sep='\t')
    else:
        pass    
        
    if (sec == 0) and (c.microsecond < 10):
        #print("m%saveInterval = " + str(m%saveInterval))
        #print("m%printInterval = " + str(m%printInterval))
        m = m+1
        #print("m = " + str(m))
        #print("sec = " + str(sec))
        #print(type(m))
        
        
    #print("i is now " + str(i) + " time is " + str(c))
    #print("n = " + str(n))
    #print("Still kickin")
    #t.sleep(1)

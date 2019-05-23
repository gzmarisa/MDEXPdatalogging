#! /bin/python3
import sys
import time as t
import datetime
from CProbe import ConductivityProbe
from TProbes import TemperatureProbes
from Scale import Scale

def fprintf(stream, format_spec, *args):
    stream.write(format_spec % args)

#def main():
    
con = ConductivityProbe(2, 9600)
#Testing methods
#con.whosmans()
#con.helpme()
#con.changeB(80000)
#con.changeP(1)
#con.whosmans()
con.openC()
#l = con.line()
#+-print(l)

T = TemperatureProbes(3, 115200)
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

printInterval = int(input("What interval (in minutes) would you like the data to be printed?"))
print(type(printInterval))


saveInterval = int(input("What interval (in minutes) would you like the data to be saved to a text file?"))

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
print("Waiting for seconds to equal 0")
time = t.localtime(None).tm_sec
    #loop for making the code start when seconds = 0
while(time != 0):
    #print("Waiting for seconds to equal 0")
    time = t.localtime(None).tm_sec            
    #print(t.localtime(None))
    #print("Still kickin")
print("SECONDS = 0!!!")

print("Cond", "Weight","HotIn", "HotOut", "ColdIn","ColdOut","Month","Day","Hour","Minute","Second",sep='\t')
    #main()
    #initialize arrays
while (True):
    print("I'm alive, I swear. Just don't ask me to complete a CAPTCHA")
        #Get current date and time
    d = datetime.date.today()
    c = datetime.datetime.now()
        #year = d.year
        #Save date, time, conductivity, weight and temp outputs to arrays
    p = e/60
    s = dd/60
    if i == 0:
        print("Case 1")
        month.append(d.month)
        dayy.append(d.day)
        hour.append(c.hour)
        minute.append(c.minute)
        second.append(c.second)
        print("Got the date and time")
        cond.append(con.line())
        print("got conductivity")
        wt.append(S.line())
        print("got weight")
        temp.append(T.line())
        print("got temps")
        print("appended all")
        print(cond[m], wt[m], temp[m], month[m], day[m], hour[m], minute[m], second[m], sep='\t')
        f=open(filename, "a+")
        print("opened file")
        f.write(str(cond[m])  + "\t" + str(wt[m]) + "\t" + temp[m] + "\t" + str(month[m]) + "\t" + str(day[m]) + "\t" + str(hour[m]) + "\t" + str(minute[m]) + "\t" + str(second[m]) + "\n")
        print("Wrote to file")
        f.close()
        print("Closed file")
        m = m+1
        
    elif (p == printInterval):
        print("Case 2")
        mon=d.month
        day=d.day
        hour=c.hour
        minn=c.minute
        sec=c.second
        conn=con.line()
        weight=S.line()
        temps=T.line()
        print(conn, weight, temps, minn, day, hour, minn, sec, sep='\t')

    elif (s == saveInterval):
        print("Case 3")
        month.append(d.month)
        dayy.append(d.day)
        hour.append(c.hour)
        minute.append(c.minute)
        second.append(c.second)
        cond.append(con.line())
        wt.append(S.line())
        temp.append(T.line())
        print(cond[m], wt[m], temp[m], month[m], dayy[m], hour[m], minute[m], second[m], sep='\t')
        f=open(filename, "a+")
        f.write(str(cond[m])  + "\t" + str(wt[m]) + "\t" + temp[m] + "\t" + str(month[m]) + "\t" + str(day[m]) + "\t" + str(hour[m]) + "\t" + str(minute[m]) + "\t" + str(second[m]) + "\n")
        f.close()
        m = m+1
        #print(second)
        #if (i>=(interval-1)):
            
            #if(i>0):
            #    averageCond = sum(cond) / float(len(cond))
            #    #For average wt.
            #    averageWT = sum(wt) / float(len(wt))
                #averageTemp = sum(float(temp)) / float(len(temp))
            #    print("Average Conductivity",averageCond, "Average Weight",averageWT, sep='\t')
            #print(type(cond[i]))
            #print(type(wt[i]))
            #print(type(temp[i]))
            #print(type(month[i]))
            
    else:
        pass
        t.sleep(1)
        #if (hour[i] == 16) & (minute[i] == 0):
        #    break
        #elif (wt[i] == 1000):
        #    break
       # else:
        #if
        #print("Test: ",cond[i], wt[i], temp[i], month[i], day[i], hour[i], minute[i], second[i], sep='\t')
    if (p == printInterval):
        e = 0
    elif (s == saveInterval):
        dd = 0
    else:
        e = e +1
        dd = dd +1
        i = i+1
        #if(i>=interval):
        #    i=0
    print("i is now " + str(i) + " time is " + str(c))
    print("e is " + str(e))
    #print("Still kickin")

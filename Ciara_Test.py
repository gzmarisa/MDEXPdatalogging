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
    
con = ConductivityProbe(0, 9600)
#Testing methods
#con.whosmans()
#con.helpme()
#con.changeB(80000)
#con.changeP(1)
#con.whosmans()
con.openC()
#l = con.line()
#+-print(l)

T = TemperatureProbes(1, 115200)
#Testing methods
#T.whosmans()
#T.helpme()
#T.changeB(80000)
#T.changeP(0)
#T.whosmans()
T.openC()
#l = T.line()
#print(l)

S = Scale(0, 19200)
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
day = []
hour = []
minute = []
second = []
cond = []
wt = []
temp = []
i = 0
m = 0;
time = ("Waiting for seconds to equal 0")
time = t.localtime(None).tm_sec
    #loop for making the code start when seconds = 0
while(time != 0):
    #print("Waiting for seconds to equal 0")
    time = t.localtime(None).tm_sec            
    #print(t.localtime(None))
    #print("Still kickin")


print("Cond", "Weight","HotIn", "HotOut", "ColdIn","ColdOut","Month","Day","Hour","Minute","Second",sep='\t')
    #main()
    #initialize arrays
while (True):
        #print("I'm alive, I swear. Just don't ask me to complete a CAPTCHA")
        #Get current date and time
    d = datetime.date.today()
    c = datetime.datetime.now()
        #year = d.year
        #Save date, time, conductivity, weight and temp outputs to arrays
    m = c.minute

    if i == 0:
        month.append(d.month)
        day.append(d.day)
        hour.append(c.hour)
        minute.append(c.minute)
        second.append(c.second)
        cond.append(con.line())
        wt.append(S.line())
        temp.append(T.line())
        f=open(filename, "a+")
        f.write(str(cond[i])  + "\t" + str(wt[i]) + "\t" + temp[i] + "\t" + str(month[i]) + "\t" + str(day[i]) + "\t" + str(hour[i]) + "\t" + str(minute[i]) + "\t" + str(second[i]) + "\n")
        f.close()
        print(cond[i], wt[i], temp[i], month[i], day[i], hour[i], minute[i], second[i], sep='\t')
        
    elif ((m/printInterval)==0) == True:
        mon=d.month
        day=d.day
        hour=c.hour
        minn=c.minute
        sec=c.second
        conn=con.line()
        weight=S.line()
        temps=T.line()
        print(conn, weight, temps, minn, day, hour, minn, sec, sep='\t')

    elif (m/saveInterval)==0 == True:
        month.append(d.month)
        day.append(d.day)
        hour.append(c.hour)
        minute.append(c.minute)
        second.append(c.second)
        cond.append(con.line())
        wt.append(S.line())
        temp.append(T.line())
        f=open(filename, "a+")
        f.write(str(cond[i])  + "\t" + str(wt[i]) + "\t" + temp[i] + "\t" + str(month[i]) + "\t" + str(day[i]) + "\t" + str(hour[i]) + "\t" + str(minute[i]) + "\t" + str(second[i]) + "\n")
        f.close() 
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
        
        #print("Test: ",cond[i], wt[i], temp[i], month[i], day[i], hour[i], minute[i], second[i], sep='\t')
    i = i +1
        
        #if(i>=interval):
        #    i=0
    #print("i is now " + str(i) + " time is " + str(c))
    
    #print("Still kickin")

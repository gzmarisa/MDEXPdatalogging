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

#loop for making the code start when seconds = 0
#time = t.localtime(None).tm_sec
#while(time != 0):
#    time = t.localtime(None).tm_sec
    #print("can you wait?")
        
#print(t.localtime(None))
#print("Still kickin")


printInterval = input("What interval (in minutes) would you like the data to be printed?")



saveInterval = input("What interval (in minutes) would you like the data to be saved to a text file?")

filename = str(input("What would you like the file name to be?"))
f = open(filename, "w+")
f.write("Cond\tWeight\tHotIn\tHotOut\tColdIn\tColdOut\tMonth\tDay\tHour\tMinute\tSecond\n")
f.close() 

print("Cond", "Weight","HotIn", "HotOut", "ColdIn","ColdOut","Month","Day","Hour","Minute","Second",sep='\t')
#main()
#initialize arrays

interval=60
month = [None] * interval
day = [None] * interval
hour = [None] * interval
minute = [None] * interval
second = [None] * interval
cond = [None] * interval
wt = [None] * interval
temp = [None] * interval
i = 0

         
while (True):
    print("I'm alive, I swear. Just don't ask me to complete a CAPTCHA")
    #Get current date and time
    d = datetime.date.today()
    c = datetime.datetime.now()
    #year = d.year
    #Save date, time, conductivity, weight and temp outputs to arrays
    month[i]=d.month
    day[i]=d.day
    hour[i]=c.hour
    minute[i]=c.minute
    second[i]=c.second
    cond[i]=float(con.line())
    wt[i]=float(S.line())
    temp[i]=T.line()
    #print(second)
    if (i>=(interval-1)):
        print(cond[i], wt[i], temp[i], month[i], day[i], hour[i], minute[i], second[i], sep='\t')
        if(i>0):
            averageCond = sum(cond) / float(len(cond))
            #For average wt.
            averageWT = sum(wt) / float(len(wt))
            #averageTemp = sum(float(temp)) / float(len(temp))
            print("Average Conductivity",averageCond, "Average Weight",averageWT, sep='\t')
        #print(type(cond[i]))
        #print(type(wt[i]))
        #print(type(temp[i]))
        #print(type(month[i]))
        f=open(filename, "a+")
        f.write(str(cond[i])  + "\t" + str(wt[i]) + "\t" + temp[i] + "\t" + str(month[i]) + "\t" + str(day[i]) + "\t" + str(hour[i]) + "\t" + str(minute[i]) + "\t" + str(second[i]) + "\n")
        f.close() 
    else:
        m = second[i] % 30
    #if (hour[i] == 16) & (minute[i] == 0):
    #    break
    #elif (wt[i] == 1000):
    #    break
   # else:
    #t.sleep(0.01)
    #print("Test: ",cond[i], wt[i], temp[i], month[i], day[i], hour[i], minute[i], second[i], sep='\t')
    i = i +1
    if(i>=interval):
        i=0
    print("i is now " + str(i) + " time is " + str(c))
    #print("Still kickin")




import sys
import time as t
import datetime
from CProbe import ConductivityProbe
from TProbes import TemperatureProbes
from Scale import Scale

def fprintf(stream, format_spec, *args):
    stream.write(format_spec % args)


def main():
    con = ConductivityProbe(2, 9600)
    con.whosmans()
    con.helpme()
    con.changeB(80000)
    con.changeP(1)
    con.whosmans()
    #con.openC()
    #l = con.line()
    #print(l)

    T = TemperatureProbes(1, 8909890)
    T.whosmans()
    T.helpme()
    T.changeB(80000)
    T.changeP(0)
    T.whosmans()
    #T.openC()
    #l = T.line()
    #print(l)

    S = Scale(0, 8909890)
    S.whosmans()
    S.helpme()
    S.changeB(80000)
    S.changeP(7)
    S.whosmans()
    #S.openC()
    #l = S.line()
    #print(l)

    #loop for making the code start when seconds = 0
    time = t.localtime(None).tm_sec
    while(time != 0):
        time = t.localtime(None).tm_sec
        #print("can you wait?")
        
    print(t.localtime(None))
    print("Month","Day","Hour","Minute","Second",sep='\t')

main()
month = []
day = []
hour = []
minute = []
second = []
i = 0
while (True):
    #print("I'm alive, I swear. Just don't ask me to complete a CAPTCHA")
    d = datetime.date.today()
    c = datetime.datetime.now()
    #year = d.year
    month.append(d.month)
    day.append(d.day)
    hour.append(c.hour)
    minute.append(c.minute)
    second.append(c.second)
    #print(second)
    m = second[i] % 30
    f = 0
    #if (m == 0):
        #f = f+1
        #print (f)
        #print(m)
    #if (f == 1) & (m==0):
    if (m==0):
        print(month[i], day[i], hour[i], minute[i], second[i], sep='\t')
    t.sleep(1)
    i = i +1 
    #print("Still kickin")




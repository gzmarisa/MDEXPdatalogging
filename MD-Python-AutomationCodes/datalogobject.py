from CProbe import ConductivityProbe
from TProbes import TemperatureProbes
from Scale import Scale
import sys
import time as t
import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class datalog:
    

    def __init__(self, filename, Cport, Tport, Sport):
        self.filename=filename
        self.Cport = Cport
        self.Tport = Tport
        self.Sport = Sport
        self.con = ConductivityProbe(Cport, 115200)
        self.con.openC()
        self.T = TemperatureProbes(Tport, 115200)
        self.T.openC()
        self.S = Scale(Sport, 19200)
        self.S.openC()
        f = open(self.filename, "w+")
        f.write("Cond\tWeight\tHotIn\tHotOut\tColdIn\tColdOut\tMonth\tDay\tHour\tMinute\tSecond\n")
        f.close()
        print("Waiting for first second of minute...")
        time = t.localtime(None).tm_sec
        while(time != 0):
            time = t.localtime(None).tm_sec
        
    def getdata(self, printInterval, saveInterval, exitWeight):
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
        print("Cond", "Weight","HotIn", "HotOut", "ColdIn","ColdOut","Month","Day","Hour","Minute","Second",sep='\t')
        d = datetime.date.today()
        c = datetime.datetime.now()
        h = c.hour
        mi = c.minute
        sec = c.second
        dayy = d.day
        mo = d.month
        conn=self.con.line()
        weight=self.S.line()
        #print(type(weight))
        temps=self.T.line()
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
                temp = self.S.line()
                if (temp!= weight and temp!="" and temp!=None):
                    weight=temp
            if (sec == 0) and (m % saveInterval == 0) and (c.microsecond < 1000):
                conn=self.con.line()
                temps=self.T.line()
                print(conn, weight, temps, mo, dayy, h, mi, sec, sep='\t')
                self.S.flushh()
                f=open(self.filename, "a+")
                f.write(str(conn)  + "\t" + str(weight) + "\t" + temps + "\t" + str(mo) + "\t" + str(dayy) + "\t" + str(h) + "\t" + str(mi) + "\t" + str(sec) + "\n")
                f.close()
                n = n+1
                self.S.flushh()
            elif (sec == 0) and (m % printInterval == 0) and (c.microsecond < 1000):
                conn=self.con.line()
                temps=self.T.line()
                print(conn, weight, temps, mo, dayy, h, mi, sec, sep='\t')
                self.S.flushh()

            else:
                pass
                
            if (sec == 0) and (c.microsecond < 100):
                m = m+1
            if (float(weight) >= float(exitWeight)):
                conn=self.con.line()
                temps=self.T.line()
                print(conn, weight, temps, mo, dayy, h, mi, sec, sep='\t')
                f=open(self.filename, "a+")
                f.write(str(conn)  + "\t" + str(weight) + "\t" + temps + "\t" + str(mo) + "\t" + str(dayy) + "\t" + str(h) + "\t" + str(mi) + "\t" + str(sec) + "\n")
                f.close()
                #self.finishup()
                break
            
    def finishup(self, email):
        #Want to call this in fuction above (getdata())
        #Look at email test for help
        #this should send an email to person inputted to tell them that
        #the experiment is over
                


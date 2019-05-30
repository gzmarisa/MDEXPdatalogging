#!
import serial
import time as t
import datetime


#opens serial port for conductivity probe
#print("Trying ACM0")
ser1 = serial.Serial('/dev/ttyACM0',115200)
#print("Connected to ACM2")
#print("Closing Ser1 just in case")
ser1.close()
#print("Opening Ser1 because, um,  duh...")
ser1.open()

#opens serial port for scale  
#print("Trying USB1")
ser2 = serial.Serial('/dev/ttyUSB0',19200)
#print("Connected to USB1")
#print("Closing Ser2 just in case")
ser2.close()
#print("Opening Ser2 because, um,  duh...")
ser2.open()

#opens serial port for temperature probes
#print("Trying ACM1")
ser3 = serial.Serial('/dev/ttyACM1',115200)
#print("Connected to ACM1")
#print("Closing Ser3 just in case")
ser3.close()
#print("Opening Ser3 because, um,  duh...")
ser3.open()
#print("starting infinite loop, again")

def main():
    #loop for making the code start when seconds = 0
    time = t.localtime(None).tm_sec
    while(time != 0):
        time = t.localtime(None).tm_sec
        #print("can you wait?")
        #print(t.localtime(None))

print("Cond\tWeight\tHotIn\tHotOut\tColdIn\tColdOut\tMonth\tDay\tHour\tMinute\tSecond\n")
        
main()
while True:
    #print("I'm alive, I swear. Just don't ask me to complete a CAPTCHA")
    
    d = datetime.date.today()
    c = datetime.datetime.now()
    year = d.year
    month = d.month
    day = d.day
    hour = c.hour
    minute = c.minute
    second = c.second
    line1 = ser1.readline().strip().decode('utf-8')
    line2 = ser2.readline().strip().rpartition(b' g')[0].decode('utf-8')
    line3 = ser3.readline().strip().decode('utf-8')
    print(line1,line2,line3,year,month,day,hour,minute,second,sep='\t')
    #t.sleep(5)
        
    #print("Still kickin")
            
  





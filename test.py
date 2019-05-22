import serial
print("Cond", "Weight","HotIn", "HotOut", "ColdIn","ColdOut","Month","Day","Hour","Minute","Second",sep='\t')

#print("Trying " + self.port + " at " + str(self.baud) + " baud")
print("trying")
ser = serial.Serial('/dev/ttyACM1',115200)
    #timeout=0.5
    #print("couldn't create serial port")
    #pass
print("Closing...just in case")
ser.close()
print("Opening again")
ser.open()
print("yeet")
#print("Conductivity Probe is connected to " + self.port)
print("connected")
l = ser.readline().strip().decode('utf-8')
print("Successfully read a line from the serial port")
print(l)
#return self.ser.readline().strip().split('\t').decode('utf-8')
print(type(l))
f = [4]
#print(type(f[1]))
f = l.split('\t')
n = []
for i in range(0, 4):
    n.append(float(f[i]))
    print(i)
print(n)

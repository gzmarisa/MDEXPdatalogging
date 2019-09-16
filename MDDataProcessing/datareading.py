import math

def main():

    file = open("MDEXP_20190418")

    A = 0.039
    lines = []
    cond = [] #conductivty list
    w = [] #weight list
    vol = [] #weight divided by 1000 to get Liters
    hin = [] #temp 1 list
    hout = [] #temp 2 list
    cin = [] #temp 3 list
    cout = [] #temp 4 list
    yr = [] #year list
    mon = [] #month list
    dy = [] #day list
    h = [] #hour list
    m = [] #minutes list
    s = [] #seconds list 
    file.readline() #reads first line so you can skip it 
    for line in file:
            #print(line.rstrip())
            orgLine = line
            line=line.rstrip().split(",")
            if (len(line) == 12):
                lines.append(orgLine)
                try:
                    cond.append(float(line[0])) # since you have decimal numbers,you wrap it in a float since integers,are only whole numbers
                except ValueError:
                    pass
                try:
                    w.append(float(line[1]))
                except ValueError:
                    pass
                try:
                    hin.append(float(line[2]))
                except ValueError:
                    pass
                try:
                    hout.append(float(line[3]))
                except ValueError:
                    pass
                try:
                    cin.append(float(line[4]))
                except ValueError:
                    pass
                try:
                    cout.append(float(line[5]))
                except ValueError:
                    pass
                try:
                    yr.append(float(line[6]))
                except ValueError:
                    pass
                try:
                    mon.append(float(line[7]))
                except ValueError:
                    pass
                try:
                    dy.append(float(line[8]))
                except ValueError:
                    pass
                try:
                    h.append(int(line[9]))
                except ValueError:
                    pass
                try:
                    m.append(int(line[10]))
                except ValueError:
                    pass
                try:
                    s.append(int(line[11]))
                except ValueError:
                    pass

    

    #tcurr1 = []           
    mcurr1 = []
    mLines = []
    wcurr = []
    exh = 0
    for i in range(len(m)):
        if ((exh+m[i]) not in mcurr1 and w[i] >= 0):
            mcurr1.append(m[i]+exh) #actual minute value
            #tcurr1.append(i+1)
            #print(tcurr1)
            if (m[i]==59):
                exh+=60
            wcurr.append(w[i])
            mLines.append(i) #placement of minute line

    tcurr1 = []
    for i in range(len(mcurr1)):
        tcurr1.append(i+1)
        #print(tcurr1)

    vol = [i / 1000 for i in wcurr] #find volume for each element in the weight list

  
    exv = 0
    for i in range(len(vol)-2):
        vol[i] += exv
        if (((vol[i+1]+exv)-(vol[i])) < 0):
            exv+=vol[i]
            
    #print('minute | volume')
    #for i in range(len(vol)):
        #print( str(tcurr[i]) + ' | ' + str(vol[i]))


    tcurr5 = tcurr1[4::5] #actual minute for every 5 mins
    print(tcurr5)
    hcurr5 = [i / 60 for i in tcurr5]
    tcurr10 = tcurr1[9::10] #actual minute for every 10 minutes
    hcurr10 = [i / 60 for i in tcurr10]
    tcurr15 = tcurr1[14::14] #actual minute for every 15 minutes
    hcurr15 = [i / 60 for i in tcurr15]
    tcurr20 = tcurr1[19::20] #actual minute for every 20 minutes
    hcurr20 = [i / 60 for i in tcurr20]
   
    #print('minute | volume')
    #for i in range(len(vol)):
        #print( str(tcurr[i]) + ' | ' + str(vol[i]))
    
    
  
    diffvol1 = []
    i1=1
    r1=math.floor((len(vol)-1)/i1)
    for i in range(r1):
        diffvol1.append(vol[i1*(i+1)]-vol[i1*(i)])


    diffvol5 = []
    i5=5
    r5=math.floor((len(vol)-1)/i5)
    for i in range(r5):
        diffvol5.append(vol[i5*(i+1)]-vol[i5*(i)])
        
    diffvol10 = []
    i10=10
    r10=math.floor((len(vol)-1)/i10)
    for i in range(r10):
        diffvol10.append(vol[i10*(i+1)]-vol[i10*(i)])

    diffvol15 = []
    i15=15
    r15=math.floor((len(vol)-1)/i15)
    for i in range(r15):
        diffvol15.append(vol[i15*(i+1)]-vol[i15*(i)])

    diffvol20 = []
    i20=20
    r20=math.floor((len(vol)-1)/i20)
    for i in range(r20):
        diffvol20.append(vol[i20*(i+1)]-vol[i20*(i)])

    #print('tcurr1 | diffvol1')
    #for i in range(len(diffvol1)):
        #print( str(tcurr20[i]) + ' | ' + str(diffvol20[i]))  


    Jw1 = []
    delt1 = (1/60)
    for i in range(len(diffvol1)):
        Jw1.append((diffvol1[i])/(A*delt1))

    Jw5 = []
    delt5 = (5/60)
    for i in range(len(diffvol5)):
        Jw5.append(diffvol5[i]/(A*delt5))

    Jw10 = []
    delt10 = (10/60)
    for i in range(len(diffvol10)):
        Jw10.append(((diffvol10[i])/(A*delt10)))
        
    Jw15 = []
    delt15 = (15/60)
    for i in range(len(diffvol15)):
        Jw15.append((diffvol15[i])/(A*delt15))

    Jw20 = []
    delt20 = (20/60)
    for i in range(len(diffvol20)):
        Jw20.append(diffvol20[i]/(A*delt20))


    #print('int | Jw20')
    #for i in range(len(Jw20)):
        #print( str(hcurr20[i]) + ' | ' + str(Jw20[i]))

                   
main()

#! /bin/python3
import sys
import time as t
import datetime
from CProbe import ConductivityProbe
from TProbes import TemperatureProbes
from Scale import Scale
from datalogobject import datalog

def main():
    printInterval = float(input("What interval (in minutes) would you like the data to be printed?   "))
    saveInterval = float(input("What interval (in minutes) would you like the data to be saved to a text file?   "))
    exitWeight = str(input("At what distillate weight would you like the program to end?   "))
    filename = str(input("What would you like the file name to be?   ")) + ".csv"
    #email = str(input("What email would you like emails to be sent to?   "))
    #For below method, it is the ending of the ports in the following order:
    #conductivity, temperature, scale
    data = datalog(filename, 1, 0, 0)
    data.getdata(printInterval, saveInterval,exitWeight)
    #data.finishup(email)
main()

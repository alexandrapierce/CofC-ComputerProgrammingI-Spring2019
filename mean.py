#Name: Alex Pierce CSCI220-03
#mean.py
#Purpose:calculates the mean of a set of numbers three different ways
#Inputs:values from user
#Outputs:rms average, harmonic mean, and geometric mean to monitor
#Certification: I certify that this lab is entirely my own work with help from CSL

import math

def rmsAvg(numList):
    #length of a list
    numValue = len(numList)
    #Loop
    total=0
    for i in range(numValue):
        # indexing a list:
        # grab individual numbers by their index using i
        val=numList[i]
        numSqr=(val**2)
        total=(total+numSqr)
    #Calculation and output
    rmsAvg=math.sqrt(total/numValue)    
    print("rms average=", round(rmsAvg,3))
    
def harmMean(numList):
    #length of a list
    numValue = len(numList)
    #Loop
    total=0
    for i in range(numValue):
        val=numList[i]
        numFrac=1/val
        total=(total+numFrac)
    #Calculation and output
    harmMean=(numValue/total)    
    print("harmonic mean=", round(harmMean,3))

def geoMean(numList):
    #length of a list
    numValue = len(numList)
    #Loop
    total=1
    for i in range(numValue):
        val=numList[i]
        total=(total*val)
        numPow=1/numValue
    #Calculation and output
    geoMean=total**numPow   
    print("geometric mean=", round(geoMean,3))

def main():
    #Purpose
    print("This code will generate the RMS average, harmonic mean, and geometric mean for a set of values.")
    #Ask user to input number of values
    numValue=int(input("Enter the number of values:"))
    print()
    # initialize a list (start w empty list)
    listOfNums = []
    for i in range(numValue):
        val=float(input("Enter value:"))
        # add val to listOfNums
        listOfNums.append(val)
    print()
    rmsAvg(listOfNums)
    harmMean(listOfNums)
    geoMean(listOfNums)

    
main()
                 
                 

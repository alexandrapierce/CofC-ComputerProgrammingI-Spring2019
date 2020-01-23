#Name:Alex Pierce CSCI220-03
#weightedAverage.py
#Purpose:get file of grades from user. Compute and output the class average
#Inputs:Ask user to enter name of file of grades 
#Outputs:Class average from individual averages
#Certification: I certify that this lab is entirely my own work with help from CS lab.

def weightedAverage():
    #Ask user for file name containing grades
    fileName=input("Enter the name of the file: ")
    infile=open(fileName, "r")
    #first loop- split lines into parts(students name and grades with weights)
    count=0
    classSum=0
    for line in infile:
        count+=1
        parts = line.split()
        name = parts[0]+" "+parts[1]
        nums= parts[2:]
        #2nd loop- calculates the averages of each student
        #multiplies grades with weights and divides total by 100
        total=0
        for i in range(0,len(nums),2):
            grade= float(nums[i])*float(nums[i+1])
            total+=grade/100
        print(str(name) + "'s average: " + "{0:.1f}".format(total))
        classSum+=total
    
    #class average calculation 
    classAvg= classSum/count
    print()
    print("Class average: ","{0:.1f}".format(classAvg))
        
        
weightedAverage()
    

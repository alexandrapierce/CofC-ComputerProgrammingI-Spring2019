#Name:Alex Pierce CSCI220-03
#closedShapes.py
#Purpose: Calculates volume and surface area of a prism and cylinder
#Inputs: values of height, length, and radius (numeric, provided by user)
#Outputs: volume and surface area of a prism and cylinder to monitor 
#Certification: I certify that this lab is entirely my own work.

import math

def prism():
    #Volume and surface area of prism
    print("This code calculates the volume and surface area of a prism.")
    print()
    #User input length and height
    length=float(input("Enter the length of any side of the base of the prism:"))
    height=float(input("Enter the height of the prism:"))
    #Calculation
    volume=((length)**2*(height))
    surfaceArea=(4*length*height+(2*length**2))
    print()
    #Output
    print("Volume of prism=", volume)
    print("Surface area of prism=", surfaceArea)
    print()

def cylinder():
    #Volume  and surface area of cylinder
    print("This code calculates the volume and surface area of a closed cylinder.")
    print()
    #User input radius and height
    radius=float(input("Enter the radius of the cylinder:"))
    height=float(input("Enter the height of the cylinder:"))
    #Calculation
    volume=math.pi*(radius**2)*height
    surfaceArea=(2*math.pi*(radius**2)+2*math.pi*radius*height)
    print()
    #output
    print("Volume of cylinder=", volume)
    print("Surface area of a cylinder=", surfaceArea)
    print()         
        
def main():
    #Lets user input the number of prisms so that the code will loop n times
    n=eval(input("Enter the number of prisms:"))
    for i in range(n):
        prism()
    #Lets user input the number of cylinders so that the code will loop n times
    n=eval(input("Enter the number of cylinders:"))
    for i in range(n):
        cylinder()

main()
        



                    

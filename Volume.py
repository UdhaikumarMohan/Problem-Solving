#Find the volume of the rectangular water tank:
#Variables Length(l), Width(w), Height(h) and Volume(vol) in meters.

#Define the function:
def Water_tank(l, w, h):

#Negative values are not allowed here, so we are going to ignore it using if condition:
    if (l<=-1) or (w<=-1) or (h<=-1):
        print("Negative values are not allowed, Please give a valid input")
        
    else:
#Apply the Mathematical formula here:
        vol = (l*w*h)
        print("The volume of the water tank is: %.3f" %vol + " m^3")
       
#User Input:
print("Inputs has been taken in unit, Meter(m)")
l = float(input("Enter the Length of the water tank: "))
w = float(input("Enter the Width of the water tank: "))
h = float(input("Enter the Height of the water tank: "))

#Calling the function:
Water_tank(l, w, h)
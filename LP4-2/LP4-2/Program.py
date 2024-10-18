Weight = int(input("Enter Weight in Kilograms" ))
Length  = int(input("Enter Length in Centimeters" ))
Width  = int(input("Enter Width in centimeters" ))
Height = int(input("Enter Height in centimeters" ))

CubMet = Length * Width * Height
if Weight <= 27 and CubMet <= 100000:
    print("Package is Good")
elif Weight > 27 and CubMet <= 100000:
    print("Package is too heavy")
elif Weight <= 27 and CubMet > 100000:
    print("Package is too Large")
elif Weight > 27 and CubMet > 100000:
    print("Package is too heavy and too large")
    
input()
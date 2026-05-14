import math
angle_deg=float(input("enter angle in degree:"))
angle_rad=math.radians(angle_deg)#convert radian
print("sine radian=",math.sin(angle_rad))
print("cosine radian=",math.cos(angle_rad))
if(math.cos(angle_rad)==0):
  print("tan radian not defined")
else:
    print("tan radian=",math.tan(angle_rad))


import math
def volumeof_sphere(radius):
    return (4/3)*math.pi*(radius**3)
r=float(input("enter any radius:"))
volume=volumeof_sphere(r)
print(f"the volume of the sphere with {r} is={volume:.2f}")

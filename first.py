import math
angle_deg=float(input("enter angle in degree:"))
angle_rad=math.radians(angle_deg)
sine=math.sin(angle_rad)
cosine=math.cos(angle_rad)
if math.isclose(cosine,0.0,abs_tol=1e-9):
    tangent="undefined"
else:
    tangent=math.tan(angle_rad)
print(f"sine({angle_rad})={sine}")
print(f"cosine({angle_rad})={cosine}")
print(f"tangent({angle_rad})={tangent}")
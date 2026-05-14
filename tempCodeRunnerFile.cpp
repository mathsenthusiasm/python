import math

def trig_functions(angle_deg):
    angle_rad = math.radians(angle_deg)
    
    sine = math.sin(angle_rad)
    cosine = math.cos(angle_rad)
    
    # Safe check for zero using math.isclose
    if math.isclose(cosine, 0.0, abs_tol=1e-9):
        tangent = "Undefined (cosine = 0)"
    else:
        tangent = math.tan(angle_rad)
    
    return sine, cosine, tangent

# Input angle
angle_deg = float(input("Enter angle in degrees: "))

# Call function
sine, cosine, tangent = trig_functions(angle_deg)

# Print results
print(f"Sine({angle_deg})   = {sine}")
print(f"Cosine({angle_deg}) = {cosine}")
print(f"Tangent({angle_deg})= {tangent}")

weight=int(input("Enter weight:"))
unit=input("L(bs) or (K)g: ")

if unit.upper()=="L":
    weight_kg = weight*0.45
    print(f"Weight in Kg is: {weight_kg}")
else:
    weight_lbs=weight*2.2
    print(f"Weight in lbs is: {weight_lbs}")

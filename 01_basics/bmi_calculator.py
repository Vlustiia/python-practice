def get_bmi_category(imt: float) -> str:
    if imt < 18.5:
        return "Underweight"
    elif imt < 25:
        return "Normal weight"
    elif imt < 30:
        return "Overweight"
    elif imt < 35:
        return "Obesity class I"
    elif imt < 40:
        return "Obesity class II"
    else:
        return "Obesity class III"


weight = float(input("Weight (kg): "))
height = float(input("Height (cm): "))

height_m = height / 100
imt = weight / (height_m ** 2)

print(f"Your BMI: {round(imt, 2)}")
print(f"Category: {get_bmi_category(imt)}")
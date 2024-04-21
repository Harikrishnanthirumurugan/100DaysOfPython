#creating Bmi Calculator

weight=float(input("Enter Your Weight : "))
height=float(input("Enter Your Height : "))
bmi=round(weight/ (height**2), 1)
if bmi<18.5:
    print(f"Your BMI is {bmi}, you are in Under weight")
elif bmi<25:
    print(f"Yout BMI is {bmi}, You are in normal weight")
elif bmi<30:
    print(f"Yout BMI is {bmi}, You are in Over weight")
elif bmi<35:
    print(f"Yout BMI is {bmi}, You are in Obese")
else:
    print(f"Yout BMI is {bmi}, You are in Clinically Obese")

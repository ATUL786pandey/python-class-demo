#**** WAP FOR BMI OF BODY****

wght=float(input("Enter Weight of your body => "))
hght=float(input("Enter your height in meter => "))

bmi=wght/hght**2

if bmi < 18:
    print ("bmi of body {} is underweight".format(bmi))
elif bmi > 18 and bmi < 22.5:
    print("bmi of body {} is normal".format(bmi))
elif bmi >22.5 and bmi < 25:
    print("bmi of body  {} is overweight".format(bmi))
else:
    print ("bmi of body {} is obese".format(bmi))

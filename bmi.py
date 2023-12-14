height = float(input("enter your height  "))
weight = float (input("enter your weight "))

bmi = weight / (height * height)

if bmi> 18.5:
   print ("underweight")
elif bmi > 18.5 and bmi < 24.5:
   print ("normal") 
elif bmi >25 and bmi < 29.9 :
   print("overweight") 
else :
   print("overweight")     
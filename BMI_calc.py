# Body mass index (BMI) is a measure of body fat based on height and weight that applies to adult men and women
#. A BMI of 25.0 or more is overweight, while the healthy range is 18.5 to 24.9

def bmi_calc(name, height_m, weight_kg):
  bmi = weight_kg / (height_m ** 2) 
  print("BMI:")
  print(bmi)
  if bmi < 25: 
    return name + " is not overweight" 
  else: 
    return name + " is overweight" 
    
name1 = "Viola" 
height_m1 = 2
weight_kg1 = 90

name2 = "Hellen" 
height_m2 = 1.8
weight_kg2 = 170

name3 = "Adams" 
height_m3 = 2.5
weight_kg3 = 160 


result1 = bmi_calc(name1, height_m1, weight_kg1) 
print(result1)
print("")
result2 = bmi_calc(name2, height_m2, weight_kg2)
print(result2)
print("")
result3 = bmi_calc(name3, height_m3, weight_kg3) 
print(result3)

#Error haddlling using try and except.
try: 
  age = int(input("Age: "))
  income = int(input("Your income: "))
  savings = income/age
  print(savings)

except ValueError: 
  print("Invalid value")

except ZeroDivisionError: 
  print("Error! Age cannot be Zero")

except NameError: 
  print("Name is not defined please check again")
  

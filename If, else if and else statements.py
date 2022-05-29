#if,else,and else if statements.
price = 1000000.00
has_good_credit = True

if has_good_credit:
  down_payment = 0.1 * price
  
else:
  down_payment = 0.2 * price
  
print(f"down payment: ${down_payment}")

#logical operators. and,or,not
#check if applicant is eligable for loan application.

has_high_savings = True
has_good_credit = False
if has_high_savings and has_good_credit:
  print("You are eligable for loan application; please proceed!")
else:
  print("You are not eligable for loan application;work on your savings or credit")
  
#OR operator
if has_high_savings or has_good_credit:
  print("You are eligable for loan application; please proceed!")
  
#not operator
if has_high_savings and not has_good_credit:
  print("You are not eligable for loan application;work on your savings or credit")

#comparison operators 
Temperature = 40
if Temperature > 30:
  print("it's a hot day")
else:
  print("its not hot day")

name = "washington"
if len(name) < 3:
 print("Name must have at least 3 characters.")
elif len(name) > 50:
  print("name must be only of a maximun of 50 characters.")
else:
  print("Name looks good!")

#weight convertor project 

weight = int(input('weight: '))
unit = input('(L)bs or (k)g')
if unit.upper() == ("L"):
  converted = weight * 0.45
  print(f"you are {converted} kilos")
else:
  converted = weight / 0.45
  print(f"You are {converted} pounds")
  



def squre(number): 
  return number*number 


result = squre(6) 
print("the result is: ")
print(result)

print("-----------------------------------------")
print("-----------------------------------------")
import calendar

# ask of month and year
year = int(input("Please Enter the year Number: "))
month = int(input("Please Enter the month Number: "))

print(calendar.month(year, month))

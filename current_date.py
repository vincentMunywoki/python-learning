from datetime import date #date class is imported from the datetime module
today = date.today() 
print("Today's date:", today) 
print("")
#current date in diffrent format. 
#dd/mm/yyyy 

d1 = today.strftime("%d/%M/%Y")
print("Today's date:",d1) 
print("") 

#textual month, date and year 
d2 = today.strftime("%B %d, %y") 
print("Today's date:",d2) 
print("") 

#year month date 
d3 = today.strftime("%y-%m-%d") 
print("Today's date:",d3) 
print("") 

#abbreviated month 
d4 = today.strftime("%b %d-%y") 
print("Today's date:", d4)

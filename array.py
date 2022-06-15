#arrays store values of the same data types.
fruits = ["watermelon", "passion", "lemon", "orange", "berry","banana","avocando"] 
fruits.append("pineapple") #adding item 
fruits.remove("passion") #removing item

print(fruits) 

fruits[0] = "groundnuts" 
print(fruits) 

x = len(fruits) #length of items in arrays  
print(x) 

cars = ["volvo", "BMW", "toyota", "benz", "ford"] 
print(cars) 

fruits.extend(cars) #combining arrays 
print(fruits)

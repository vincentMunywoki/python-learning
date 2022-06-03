#program to determine the largest number

numbers = [2,5,3,4,7,8,9,0,6,7,8,5,4,3,2,4,6,7,12,14,45,65,78,98,23,45,67,89,90,96,97,45,23]
max = numbers[0]
for number in numbers: 
  if number > max:
    max = number
print(f"lagest number is: {max}")

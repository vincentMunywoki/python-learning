#simple calculator program
num1 = int(input("Enter first number: "))
print("which operation do you want to use?")
operation = input("""
  + for addition 
  - for subtraction
  / for division
  * for multiplication
  """)
num2 = int(input("Enter second number: "))
if operation == '+':
    result = num1 + num2
    print('{} + {} = {}'.format(num1,num2,result))
    
elif operation == '-':
  print('{} - {} = {}'.format(num1,num2,result))

elif operation == '/':
  print('{} / {} = {}'.format(num1,num2,result))

elif operation == '*':
  print('{} * {} = {}'.format(num1,num2,result))
  
else:
  print("Oops! That's invalid operator")
  

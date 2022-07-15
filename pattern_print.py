#simple python program to output below pattern.
#1
#2 1
#3 2 1
#4 3 2 1
#5 4 3 2 1 

def patttern_3(rows):
  for i in range(1, rows + 1):
    for j in range(i,0, -1):
      print(j,end="")
    print("")

#n = 5
#to take the input from the user type
n = eval(input("Enter the number of rows: "))
patttern_3(n)

my_list = []
i = 0
item = input("Enter number of items to add in a list: ")
while len(my_list) < int(item): 
  item = input("Enter item {}: ".format(i+1))
  my_list.append(item)
  i = i + 1 
print(my_list)

#program to print maximum of three numbers. 
def maximum(a,b,c):
  if a >= b:
    return a 
  elif a >= c:
    return a
  elif b >= c:
    return b
  else:
    return c
a = 1
b = 0
c = 50
print(maximum(a,b,c))

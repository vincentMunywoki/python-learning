class person: 
  def __init__(self, name, age): 
   self.name = name 
   self.age = age 

  def myfun(self): 
    print("Hello my name is " + self.name)
    print(self.name + " is my good name")
    self.name 
    self.age 

p1 = person("John",50 ) 
p1.age = 35
p1.name = "victor" # modifying object properties.
p1.myfun() 

p2 = person("joseph",40 ) 
p2.myfun()

print(p1.age)
print(p2.name)
del p2 

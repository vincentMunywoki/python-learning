#__init__ function in classes 
class Person: 
  def __init__(self, name, age): 
    self.name = name 
    self.age = age 

  def My_Fun(self): 
    print("Hello my name is " + self.name) 
    print(self.name)
    print(self.age) 
    print("--------")
    print("--------")

    


P1 = Person("john", 50)
P1.My_Fun()
P2 = Person("Hellen", 35)
P2.My_Fun()
P3 = Person("Vincent", 25)
P3.My_Fun()

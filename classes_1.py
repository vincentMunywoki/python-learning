class Robot: 
  def __init__(self, name, color, weight): # constructor  
    self.name = name #name,color and weight are attributes
    self.color = color 
    self.weight = weight 
    
  def introduce_self(self): 
      print("My name is " + self.name) 
      #print("I love color " + self.color)
    
#r1 = Robot() 
#r1.name = "Tom"
#r1.color = "red" 
#r1.weight = 30 

#r2 = Robot() 
#r2.color = "blue" 
#r2.weight = 40 

r1 = Robot("Tom", "Red", 30)
r2 = Robot("Jerry", "Blue", 40) 

class Person: 
  def __init__(self, n, p, i): 
    self.name = n 
    self.personallity = p  
    self.is_sitting = i 

  def sit_down(self): 
    self.is_sitting = True 

  def stand_up(self): 
    self.is_sitting = False 


p1 = Person("Alice", "Aggressive", True)
p2 = Person("Becky", "Talkative", False)

p1.robot_owned = r2 
p2.robot_owned = r1 

p1.robot_owned.introduce_self()
p2.robot_owned.introduce_self() 

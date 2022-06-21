# Parent class is the class being inherited from, also called base class. 
# Create a class named Person, with firstname and lastname properties, and a printname method: 

class Person: # parent class 
  def __init__(self, fname, lname): 
    self.firstname = fname 
    self.lastname = lname 

  def printname(self): # method 
    print(self.firstname, self.lastname) 

class student(Person): #child class. 
   def __init__(self, fname, lname, year):
     super().__init__(fname, lname)#super() function will make the child class inherit all the methods and properties from its parent:
     self.graduationyear = year
   def welcome(self):
    print("welcome", self.firstname, self.lastname, "to the class of",
        self.graduationyear)

x = student("Victor", "rono", 2021)
x.welcome() 
y = student("vincent", "Kyengo", 2021) 
y.welcome() 
z = student("Hellen", "Purity", 2021)
z.welcome() 

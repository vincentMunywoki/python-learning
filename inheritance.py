# Parent class is the class being inherited from, also called base class. 
# Create a class named Person, with firstname and lastname properties, and a printname method: 

class Person: # parent class 
  def __init__(self, fname, lname): 
    self.firstname = fname 
    self.lastname = lname 

  def printname(self): # method 
    print(self.firstname, self.lastname) 

class student(Person): #child class. 
   def __init__(self, fname, lname):
     Person.__init__(self, fname, lname)

x = Person("Victor", "rono")
x.printname() 
y = Person("vincent", "Kyengo") 
y.printname() 
z = Person("Hellen", "Purity")
z.printname()

#inheritance

class student: # Defining the name & class that is a template or blueprint
        def __init__(self, name, roll_no): # this is a standard oop constructor

            self.name= name # properties to add in class for further use
            self.roll_no = roll_no

        def printproperty(self): #method to print properties defined in it
            print(self.name, self.roll_no) # properties

class person(student): # another class inherited from parent class
     pass
    
obj1=person("ali", 22)
obj1.printproperty()


# std1 = student("ali", 12)# this is object
# print(std1.name, std1.roll_no)
# std1.printproperty()

class person(student):
     def printproperty(self):
          print("This is me")
          return super().printproperty()
     


class Department:
    def __init__(self,library, Lecture_Rooms):
         self.library= library
         self.Lecture_Rooms= Lecture_Rooms

    def printproperty(self):
         print(self.library, self.Lecture_Rooms)
    
class Univerity(Department):  # Inherited Class From Parrent
     def printproperty(self):
          print("Here overriding the parent class by print method")
          return super().printproperty() #method is used to get properties from parent

obj=Department("Books", "Classes") #object that is getting the class 
obj.printproperty()

obj1=Univerity("Books", "Classes") #object using child class department
obj1.printproperty() # method to print property using print method


#Procedural programming or functional 
#Object oriented Programming ....classes and objects 
class student:
    name="ali"
    roll_no= 12
std1= student()
std1.name
print(std1.name)
 

 # Use of Constructor
#class student:
    #def__init__(self)
    #pass
      
# Values & Methods
class student:
        def __init__(self, name, roll_no):

            self.name= name
            self.roll_no = roll_no

        def printproperty(self):
            print(self.name, self.roll_no)
std1 = student("ali", 12)# this is object
print(std1.name, std1.roll_no)
std1.printproperty()


class result:
     def __init__(self, marks , grade):
          self.marks= marks
          self.grade= grade

sbj1 = result(50, "A")
print(sbj1.marks, sbj1.grade)


class Data:
     def __init__(self, product , sales):
          self.product= product
          self.sales= sales

sale = Data("Toys" , 20)
print(sale.product, sale.sales)

        

# Defining the Car class
class Car:
    # Constructor to initialize properties
    def __init__(self, brand, color, speed):
        self.brand = brand
        self.color = color
        self.speed = speed

    # Method to display car details
    def show_details(self):
        print(f"This is a {self.color} {self.brand} car with a top speed of {self.speed} km/h.")

    # Method to simulate driving
    def drive(self):
        print(f"The {self.brand} is now driving at {self.speed} km/h.")

# Creating an object of Car class
my_car = Car("Toyota", "Red", 180)

# Calling methods using the object
my_car.show_details()
my_car.drive()


class car:
    def __init__(self, brand, color):
          self.brand= brand
          self.color=color
    def printproperty(self):
         print(self.brand)
         print(self.color)
         
my_car = car("Toyota", "Red")
my_car.printproperty()

          
          



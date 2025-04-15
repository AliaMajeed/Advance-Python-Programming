#Object oriented Programming
#Create a class and constructor
#Store values in an object
#Access them directly or via a method
  
# Example 1
class student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def printproperty(self):
        print(self.name, self.roll_no)

# Creating an object of the student class
std1 = student("ali", 12)

# Printing values directly from the object
print(std1.name, std1.roll_no)

# Calling a method to print the same values
std1.printproperty()

# Example 2
class result:
    def __init__(self, marks, grade):
        self.marks = marks
        self.grade = grade

    def show_result(self):
        print(self.marks, self.grade)


sbj1 = result(50, "A")
sbj1.show_result()  


#Example 3
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def car_info(self):
        print(self.brand, self.model, self.year)

# Creating an object of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Calling the method to show car information
my_car.car_info()



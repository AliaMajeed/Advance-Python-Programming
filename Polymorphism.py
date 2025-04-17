class Animal:
    def make_sound(self):
        print("Some animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

# Create a list of objects
animals = [Animal(), Dog(), Cat()]

# Loop through the list and call make_sound
for animal in animals:
    animal.make_sound()



class Student:
    def coder(self):
        print('programming class')

class Ali:
    def coder(self):
        print('programming class')

class Ahmad:
    def coder(self):
        print('coder class')

def call_coder(obj):
    obj.coder()

# Create objects
s = Student()
a = Ali()
ah = Ahmad()

# Loop through objects (polymorphism)
for obj in [s, a, ah]:
    call_coder(obj)



class Student:
    def coder (self):
        print("I'm the student")

class Teacher:
    def coder (self):
        print("i'm the teacher here")

class Parent:
    def coder (self):
        print("I'm the parent")

# def call_coder(obj):
#     obj.coder()


obj1= Student()
obj2= Teacher()
obj3= Parent()

# for obj in [obj1, obj2,obj3]:
#     call_coder(obj)
print(obj1)
print(obj2)
print(obj3)
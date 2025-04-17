# class Animal:
#     def _init_(self,name,sound):
#         self.name=name
#         self.sound=sound

#     def make_sound(self):
#         print(" some Animal sound")


# obj1=Animal('dog','bark')   
# obj1.make_sound()

# class Dog(Animal):
#     def make_sound(self):
#         print("bark")
#         super().make_sound()

# obj2=Dog('dog','bark')
# obj2.make_sound()


# class Cat(Animal):
#     def make_sound(self):
#         print('meow')
    
# obj3=Cat('cat','meow')
# obj3.make_sound()





# Define the Animal class
class Animal:
    def make_sound(self):
        print("Some animal sound")

class Dog(Animal):
    def make_sound(self):
        super().make_sound()  
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

# Create objects and call the make_sound() method
animal = Animal()
dog = Dog()
cat = Cat()

print("Animal sound:")
animal.make_sound()

print("Dog sound:")
dog.make_sound()

print("Cat sound:")
cat.make_sound()
# Operator overloading is a concept mainly from object-oriented programming (OOP) where you 
# define or change the behavior of standard operators (like +, -, *, etc.) 
# for user-defined types (classes).

# In simpler words:
# Instead of using an operator only with basic types (like numbers), you can teach it how 
# to work with your own classes.
#lets overload the + multiplication operator?

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __add__(self, other):
        return (self.name, other.name, self.marks, other.marks)
    
    def __str__(self):
        return f"{self.name}, {self.marks}"

c1 = Student(2, 3)
c2 = Student(7, 4)
c3 = c1 + c2
print(c3)



#lets overload the * multiplication operator?
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Overloading * operator
    def __mul__(self, other):
        return Student(self.name + " & " + other.name, self.marks * other.marks)

    def __str__(self):
        return f"{self.name}: {self.marks} marks"

s1 = Student("Ali", 5)
s2 = Student("Sara", 4)
s3 = s1 * s2  # Overloaded * operator
print(s3)


#lets overload the - multiplication operator?
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Overloading - operator
    def __sub__(self, other):
        return Student(self.name + " vs " + other.name, self.marks - other.marks)

    def __str__(self):
        return f"{self.name}: {self.marks} marks"

s1 = Student("Ali", 90)
s2 = Student("Sara", 85)
s3 = s1 - s2   # Overloaded - operator
print(s3)


#lets overload the / multiplication operator?
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Overload / operator
    def __truediv__(self, other):
        avg_marks = (self.marks + other.marks) / 2
        return Student(self.name + " / " + other.name, avg_marks)

    def __str__(self):
        return f"{self.name}: {self.marks} marks"

s1 = Student("Ali", 80)
s2 = Student("Sara", 90)
s3 = s1 / s2    # Using overloaded /
print(s3)


  
    
    


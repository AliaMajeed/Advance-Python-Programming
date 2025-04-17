class student:
    def study(self):
        print("lets study")

class classroom:
    def __init__(self):
        self.Ali= student()
        print("we are goint to study python")

obj = classroom()
obj.Ali.study()

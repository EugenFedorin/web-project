
class NewClass():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f'{self.name} {self.age} {self.gender}'



new = NewClass("John", 21, "Male")
print(new)

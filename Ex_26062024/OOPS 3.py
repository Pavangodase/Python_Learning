class Student:
    age = None
    name = None

    def __init__(self,name = "Pavan" ,age=26):
        self.age = age
        self.name=name



age1 = Student(name="Shravan",age = 28)
age2 = Student()

print(age1.age)
print(age1.name)

print(age2.age)
print(age2.name)
class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age
# the above is called dundo method
pupil = Student('ronald',30)
print(pupil.name)
print(pupil.age)
pupil2 = Student('james',40)
print(pupil2.name)
print(pupil2.age)

# # function is called method in a class, method gives action while attribute gives identity
class Car():
    def _init_(self,color,make,model,doors):
        self.color = color
        self.make = make
        self.model = model
        self.doors = doors
    def decscription(self):
        return(f'A {self.color} {self.make} {self.model} with {self.doors}')
fav_car = Car('blue',2024, 'lambogini', 'jet engine')
# print ('a blue 2024 lambogini with jet engine is my favourite car')
# # print(f'A {fav_car.color} {fav_car.make} {fav_car.model} with {fav_car.doors} is my favourite car')
# toyota = Car('black', 2024, 'camry', 'portable interior decorations')
# print(f'A {toyota.color} {toyota.make} {toyota.model} with {toyota.doors} is my favourite car')


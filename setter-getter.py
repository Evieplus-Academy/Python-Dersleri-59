class Person:
    def __init__(self, name, birthdate, city):
        self.name = name
        self.birthdate = birthdate
        self.city = city

    def __str__(self):
        return f"{self.name}, {self.birthdate}, {self.city}"


person1 = Person("Ahmet", "05-05-1995", "İstanbul")
person2 = Person("Ayşe", "04-04-1994", "İzmir")

print(person1)
print(person2)

setattr(person1, "name", "Mehmet")
setattr(person1, "surname", "Aslan")

print(person1.__dict__)
print(person2.__dict__)

surname = getattr(person1, "surname")
print(surname)
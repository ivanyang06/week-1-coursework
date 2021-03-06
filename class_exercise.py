class Person():
    def __init__ (self, name, height, strength, health_points):
        self.name = name
        self.height = height
        self.strength = strength
        self.health_points = health_points
    
    def __str__ (self):
        return f"{self.name} {self.health_points}"
    
    def introduce(self):
        return f"Hello, my name is {self.name}"

    def punch(self, person):
        person.health_points -= 10
    
    def eat(self):
        self.health_points = 100

george = Person("george", 69, 0, 10)
david = Person("david", 99999, -1, 11)

print(george)
print(david)

print(george.introduce())
print(david.introduce())

george.punch(david)
david.punch(david)

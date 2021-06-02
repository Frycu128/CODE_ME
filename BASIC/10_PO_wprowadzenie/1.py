class Dog:
    def __init__(self, name, bred, age):
        self.name = name
        self.type = bred
        self.age = age

    def get(self):
        return 'hau' * self.age

    def put(self):
        return f'tail of {self.name} wag.'


Alaska = Dog('Alaska', 'Alaskan malamute', 9)
Atos = Dog('Atos', 'Alaskan malamute', 1)

print(Alaska.__dict__)
print(Atos.__dict__)

class Animals:
    def who_we_are(self):
        print('We are animals!')


class Mammals(Animals):
    def who_you_are(self):
        print("I'm a mammal!")


class Dog(Mammals):
    def bark(self):
        print("hau hau hau..")


class Cat(Mammals):
    def sound(self):
        print("miauuuuu...")


class Human(Mammals):
    def what_you_can_do(self):
        print('I can think logically better than anyone!')


first_dog = Dog()
first_cat = Cat()
first_human = Human()

first_dog.who_you_are()
first_cat.who_you_are()
first_human.who_you_are()

first_dog.who_we_are()
first_cat.who_we_are()
first_human.who_we_are()

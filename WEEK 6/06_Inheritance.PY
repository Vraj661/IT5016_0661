class Animal:
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def Bark(self):
        print(f"{self.name} barks .")
        
my_dog = Dog("Bunty")
my_dog.speak()
my_dog.Bark()      
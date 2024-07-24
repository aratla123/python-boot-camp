class Animal:
    def speak():
        return "Animal is speaking"

class Dog(Animal):
    def Bark():
       return "Bow.."
    
class Puppy(Dog):
    def Puppy_speak():
        return "i am Puppy"
obj1=Animal
obj2=Dog
obj3=Puppy

print(obj1.speak())
print(obj2.Bark())
print(obj3.Puppy_speak())
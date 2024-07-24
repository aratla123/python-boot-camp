class Grandpa:
    def speak():
        return "hey"
class Father(Grandpa):
    def speak_f():
        return "hello"
class Son(Father):
    def speak_s():
        return "whats"
class Kid(Son):
    def speak_k():
        return "the matter"
obj1=Grandpa
obj2=Father
obj3=Son
obj4=Kid
print(obj1.speak())
print(obj2.speak_f())
print(obj3.speak_s())
print(obj4.speak_k())
        
          
class Father:
    def father_speak():
        return "Father class"
class Mother:
    def mother_speak():
        return "mother class"
class Kid:
    def kid_speak():
        return "I have properties"
obj1=Father
obj2=Mother
obj3=Kid
print(obj1.father_speak())
print(obj2.mother_speak())
print(obj3.kid_speak())

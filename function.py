def hello(name):
    return "Hello, " + name

name = input("Enter Your Name : ")
print(hello(name))

class Person:
    def __init__(self):
        pass
    
    def P1(self,name:str,age:int):
        self.name=name
        self.age = age
        return f"{name} : {age}"
    

p = Person()
print(p.P1("hitesh",21))


class Student:
    name = ''
    age = 0
    def __init__(self,name,age):
        self.name = name;
        self.age = age;
    def getName(self):
        return self.name;
    def getAge(self):
        return self.age;
    def setName(self,name):
        self.name = name;
    def setAge(self,age):
        self.age = age;

student1 = Student("rafi",22)
print(f"{student1.getName()} is {student1.getAge()} years old ")
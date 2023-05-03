class Student:
    name = '이름'
    age = 12

    def my_sum(self, a, b):
        return a+b

    def __init__(self, name, age):
        self.name = name
        self.age = age


jaegeon = Student()
jaegeon.name = "연제건"
jaegeon.age = '30'
print(jaegeon.name)
print(jaegeon.age)

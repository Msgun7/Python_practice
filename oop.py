class Car():
    def __init__(self, model, color):
        self.model = model
        self.color = color
        self.speed = 0

    def accelerate(self):
        self.speed += 10
        print(f"액셀을 밟습니다.현재 속도는 {self.speed}입니다.")

    def brake(self):
        self.speed = 0
        print(self.speed)

    def get_speed(self):
        return self.speed


car = Car("제네시스", "red")
car.accelerate()
car.accelerate()
car.brake()
car.accelerate()
car.accelerate()
print(car.get_speed())
# 함수에는 괄호가 기본으로 들어가야함

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("동물의 울음소리")


class Dog(Animal):
    def speak(self):
        print("멍")


class Cat(Animal):
    def speak(self, num=5):
        word = "냥"
        print(f"{word*num}")


dog = Dog("토리", "7")
cat = Cat("레오", "5")

cat.speak(50)
dog.speak()

## 함수(def)내부에 print문을 써놓은 경우 인스턴스의 함수만으로 출력이 가능하다.

class Shape:
    def get_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width


circle = Circle(8)
print(circle.get_area())

# 함수(def)내부에 return으로 받은 값은 클래스 밖에서 출력할 때 print문을 써서 출력해야한다.
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
